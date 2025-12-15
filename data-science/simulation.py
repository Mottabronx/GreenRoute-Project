import time
import random
import requests
import polyline # Librería nueva para decodificar rutas
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# --- CONFIGURACIÓN FIREBASE ---
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
print("🔌 Conectado a Firebase Firestore.")

# --- NUEVA FUNCIÓN: OBTENER RUTA REAL (OSRM) ---
def get_road_route(start_coords, end_coords):
    """
    Consulta a OSRM una ruta real de auto entre dos puntos.
    Retorna una lista de tuplas [(lat, lng), (lat, lng), ...]
    """
    # OSRM usa formato: longitud,latitud
    start_str = f"{start_coords[1]},{start_coords[0]}"
    end_str = f"{end_coords[1]},{end_coords[0]}"
    
    url = f"http://router.project-osrm.org/route/v1/driving/{start_str};{end_str}?overview=full"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # La geometría viene codificada en un string extraño, 'polyline' lo traduce
        encoded_geometry = data['routes'][0]['geometry']
        route_points = polyline.decode(encoded_geometry)
        
        print(f"🗺️ Ruta calculada: {len(route_points)} puntos GPS encontrados.")
        return route_points
    except Exception as e:
        print(f"❌ Error obteniendo ruta: {e}")
        return [start_coords, end_coords] # Fallback a línea recta si falla

# --- CLASE CAMIÓN ACTUALIZADA ---
class HydrogenTruck:
    def __init__(self, truck_id, route_name, start_coords, end_coords):
        self.truck_id = truck_id
        self.route_name = route_name
        
        # En lugar de calcular mates, guardamos la lista de puntos reales
        self.route_points = get_road_route(start_coords, end_coords)
        self.current_index = 0 # En qué punto de la carretera vamos
        
        # Posición inicial
        self.current_lat = self.route_points[0][0]
        self.current_lng = self.route_points[0][1]
        
        self.speed = 0
        self.h2_level = 100.0
        self.status = "STOPPED"

    def update_physics(self):
        """Avanza al siguiente punto de la carretera real"""
        
        # Si llegamos al final de la lista, detenemos el camión
        if self.current_index >= len(self.route_points) - 1:
            self.status = "ARRIVED"
            self.speed = 0
            return

        # AVANZAR: Saltamos de 5 en 5 puntos para que no vaya tan lento
        # (OSRM devuelve puntos muy pegados, paso a paso)
        self.current_index += 4 
        
        # Asegurarnos de no pasarnos del arreglo
        if self.current_index >= len(self.route_points):
            self.current_index = len(self.route_points) - 1

        # Actualizar coordenadas exactas del mapa
        next_point = self.route_points[self.current_index]
        self.current_lat = next_point[0]
        self.current_lng = next_point[1]
        
        # Física simulada
        self.speed = round(80 + random.uniform(-5, 10), 1) # ~80 km/h
        self.status = "MOVING"
        
        # Consumo de combustible
        self.h2_level -= 0.05
        if self.h2_level < 0: self.h2_level = 0

    def send_telemetry(self):
        data = {
            "truck_id": self.truck_id,
            "route": self.route_name,
            "speed_kmh": self.speed,
            "h2_level_percent": round(self.h2_level, 2),
            "location": {
                "lat": self.current_lat,
                "lng": self.current_lng
            },
            "status": self.status,
            "last_updated": firestore.SERVER_TIMESTAMP
        }
        db.collection("telemetry").document(self.truck_id).set(data)
        print(f"📍 {self.truck_id} en Ruta 68 | Lat: {self.current_lat:.4f}...")

if __name__ == "__main__":
    # Coordenadas exactas
    santiago_centro = (-33.4429, -70.6539) # Cerca de La Moneda
    puerto_valpo = (-33.0365, -71.6293)    # Puerto

    truck = HydrogenTruck("H2-TRUCK-01", "SCL->VAP", santiago_centro, puerto_valpo)
    
    print("🚀 Iniciando Simulación Realista...")
    
    try:
        while True:
            truck.update_physics()
            truck.send_telemetry()
            # Actualizamos cada 1 segundo para que se vea fluido en el mapa
            time.sleep(1) 
            
    except KeyboardInterrupt:
        print("Stop.")