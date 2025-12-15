<template>
  <q-page class="p-6 bg-slate-50">

    <div class="mb-8">
      <h1 class="text-2xl font-bold text-slate-800">Resumen de Operaciones</h1>
      <p class="text-slate-500">Monitoreo de flota de Hidrógeno Verde - Tiempo Real</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">

      <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 flex items-center justify-between">
        <div>
          <div class="text-slate-400 text-sm font-medium mb-1">Vehículos en Ruta</div>
          <div class="text-3xl font-bold text-slate-800">12<span class="text-lg text-slate-400 font-normal">/15</span></div>
        </div>
        <div class="bg-blue-50 p-3 rounded-lg text-blue-600">
          <q-icon name="local_shipping" size="24px" />
        </div>
      </div>

      <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 flex items-center justify-between">
        <div>
          <div class="text-slate-400 text-sm font-medium mb-1">Eficiencia H2</div>
          <div class="text-3xl font-bold text-green-600">94%</div>
        </div>
        <div class="bg-green-50 p-3 rounded-lg text-green-600">
          <q-icon name="bolt" size="24px" />
        </div>
      </div>

      <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 flex items-center justify-between">
        <div>
          <div class="text-slate-400 text-sm font-medium mb-1">Alertas Criticas</div>
          <div class="text-3xl font-bold text-red-500">2</div>
        </div>
        <div class="bg-red-50 p-3 rounded-lg text-red-600">
          <q-icon name="warning" size="24px" />
        </div>
      </div>

      <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 flex items-center justify-between">
        <div>
          <div class="text-slate-400 text-sm font-medium mb-1">CO2 Ahorrado</div>
          <div class="text-3xl font-bold text-slate-800">850 <span class="text-sm font-normal">kg</span></div>
        </div>
        <div class="bg-teal-50 p-3 rounded-lg text-teal-600">
          <q-icon name="forest" size="24px" />
        </div>
      </div>
    </div>

    <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 flex items-center justify-between">
        <div>
          <div class="text-slate-400 text-sm font-medium mb-1">Usuarios (PostgreSQL)</div>
          <div class="text-3xl font-bold text-slate-800">{{ userCount }}</div>
          <div class="text-xs mt-1" :class="statusColor">{{ systemStatus }}</div>
        </div>
        <div class="bg-indigo-50 p-3 rounded-lg text-indigo-600">
          <q-icon name="group" size="24px" />
        </div>
      </div>

    <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
        <div class="flex justify-between items-center mb-4">
          <h3 class="font-bold text-slate-700">Telemetría H2-01</h3>
          <q-badge :color="truckData.status === 'MOVING' ? 'green' : 'grey'">
            {{ truckData.status }}
          </q-badge>
        </div>

        <div class="space-y-4">
          <div>
            <div class="flex justify-between text-xs text-slate-500 mb-1">
              <span>Velocidad Actual</span>
              <span>{{ truckData.speed }} km/h</span>
            </div>
            <q-linear-progress :value="truckData.speed / 120" color="blue" track-color="blue-1" class="rounded-full" />
          </div>

          <div>
            <div class="flex justify-between text-xs text-slate-500 mb-1">
              <span>Tanque H2</span>
              <span>{{ truckData.h2_level }}%</span>
            </div>
            <q-linear-progress
              :value="truckData.h2_level / 100"
              :color="truckData.h2_level < 20 ? 'red' : 'green'"
              track-color="green-1"
              class="rounded-full"
            />
          </div>
        </div>
      </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

      <div class="lg:col-span-2 bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden h-96 relative z-0">

        <l-map
          ref="map"
          v-model:zoom="zoom"
          :center="[truckData.lat, truckData.lng]"
          :use-global-leaflet="false"
        >
          <l-tile-layer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            layer-type="base"
            name="OpenStreetMap"
          ></l-tile-layer>

          <l-marker :lat-lng="[truckData.lat, truckData.lng]">

            <l-icon
              :icon-size="[40, 40]"
              :icon-anchor="[20, 20]"
              icon-url="https://cdn-icons-png.flaticon.com/512/2554/2554978.png"
            />

            <l-popup>
              <div class="text-center">
                <b>H2-TRUCK-01</b><br>
                Ruta: Santiago - Valpo<br>
                Carga: {{ truckData.h2_level }}%
              </div>
            </l-popup>
          </l-marker>
        </l-map>

        <div class="absolute top-4 right-4 bg-white/90 backdrop-blur px-3 py-1 rounded-md text-xs font-bold text-slate-600 border border-slate-200 z-[1000]">
          Live GPS Tracking
        </div>
      </div>

      <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
        <h3 class="font-bold text-slate-800 mb-4">Bitácora de Eventos</h3>

        <div class="space-y-4">
          <div class="flex gap-3 items-start pb-4 border-b border-slate-100 last:border-0">
            <div class="mt-1 w-2 h-2 rounded-full bg-red-500"></div>
            <div>
              <div class="text-sm font-bold text-slate-700">Presión Baja - Camión H2-04</div>
              <div class="text-xs text-slate-400">Hace 10 minutos • Ruta 68</div>
            </div>
          </div>

          <div class="flex gap-3 items-start pb-4 border-b border-slate-100 last:border-0">
            <div class="mt-1 w-2 h-2 rounded-full bg-green-500"></div>
            <div>
              <div class="text-sm font-bold text-slate-700">Llegada a Destino - Camión H2-01</div>
              <div class="text-xs text-slate-400">Hace 32 minutos • Centro Logístico</div>
            </div>
          </div>

          <div class="flex gap-3 items-start">
            <div class="mt-1 w-2 h-2 rounded-full bg-blue-500"></div>
            <div>
              <div class="text-sm font-bold text-slate-700">Inicio de Carga - Camión H2-03</div>
              <div class="text-xs text-slate-400">Hace 1 hora • Planta Hidrógeno</div>
            </div>
          </div>
        </div>

      </div>

    </div>

  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { api } from 'boot/axios'; // Importamos la instancia configurada
import { doc, onSnapshot } from 'firebase/firestore';
import { db } from 'boot/firebase';
import 'leaflet/dist/leaflet.css';
import { LMap, LTileLayer, LMarker, LPopup, LIcon } from '@vue-leaflet/vue-leaflet';

// Variables para el camión
const truckData = ref({
  speed: 0,
  h2_level: 0,
  status: 'OFFLINE',
  lat: -33.4489, // Coordenada inicial (Santiago Centro)
  lng: -70.6693
});

// Variables reactivas
const userCount = ref(0);
const systemStatus = ref('Desconectado');
const statusColor = ref('text-red-500');
const zoom = ref(13);

// Función para escuchar Firebase en Tiempo Real
function subscribeToTruck() {
  const docRef = doc(db, "telemetry", "H2-TRUCK-01");

  onSnapshot(docRef, (docSnap) => {
    if (docSnap.exists()) {
      const data = docSnap.data();
      truckData.value = {
        speed: data.speed_kmh,
        h2_level: data.h2_level_percent,
        status: data.status,
        // Aquí capturamos la posición que envía Python
        lat: data.location.lat,
        lng: data.location.lng
      };
    }
  });
}

// Función para obtener usuarios desde Java
async function fetchUsers() {
  try {
    console.log("Intentando conectar con Spring Boot...");
    // Petición GET a tu endpoint
    const response = await api.get('/api/users');

    // Si llegamos aquí, ¡éxito!
    console.log("Datos recibidos:", response.data);

    // Actualizamos la vista
    userCount.value = response.data.length; // Cantidad de usuarios en la lista
    systemStatus.value = 'Conectado (Online)';
    statusColor.value = 'text-green-600';

  } catch (error) {
    console.error("Error al conectar:", error);
    systemStatus.value = 'Error de Conexión';
    statusColor.value = 'text-red-600';
  }
}

// Ejecutar cuando la página carga
onMounted(() => {
  void fetchUsers();
  subscribeToTruck();
});
</script>
