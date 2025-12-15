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

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      
      <div class="lg:col-span-2 bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden h-96 relative">
        <div class="absolute inset-0 bg-slate-100 flex items-center justify-center flex-col">
          <q-icon name="map" size="48px" class="text-slate-300 mb-2" />
          <span class="text-slate-400 font-medium">Mapa de Rutas (Google Maps / Leaflet)</span>
          <span class="text-xs text-slate-400 mt-1">Se integrará en la Fase 3</span>
        </div>
        
        <div class="absolute top-4 left-4 bg-white/90 backdrop-blur px-3 py-1 rounded-md text-xs font-bold text-slate-600 border border-slate-200">
          Vista en Vivo
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
// Aquí irá la lógica para traer datos de la API más adelante
</script>