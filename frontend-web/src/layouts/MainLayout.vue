<template>
  <q-layout view="lHh Lpr lFf" class="bg-slate-50">
    
    <q-header elevated class="bg-white text-slate-800 border-b border-slate-200">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
          class="text-slate-600"
        />

        <q-toolbar-title class="flex items-center gap-2 font-bold text-slate-700">
          <q-icon name="local_shipping" class="text-green-600" size="28px" />
          <span>GreenRoute <span class="text-green-600 text-sm font-normal">Analytics</span></span>
        </q-toolbar-title>

        <div class="flex items-center gap-3">
          <div class="text-right hidden sm:block">
            <div class="text-sm font-bold">Ingeniero Demo</div>
            <div class="text-xs text-slate-500">Admin Flota</div>
          </div>
          <q-avatar size="36px" class="bg-green-100 text-green-700 font-bold cursor-pointer">
            JD
          </q-avatar>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class="bg-slate-900 text-slate-300"
    >
      <div class="p-4 text-xs font-bold text-slate-500 uppercase tracking-wider">
        Menú Principal
      </div>

      <q-list padding>
        <q-item 
          v-for="link in linksList" 
          :key="link.title" 
          clickable 
          v-ripple
          class="hover:bg-slate-800 hover:text-green-400 transition-colors rounded-r-full mr-2 mb-1"
        >
          <q-item-section avatar>
            <q-icon :name="link.icon" />
          </q-item-section>

          <q-item-section>
            <q-item-label>{{ link.title }}</q-item-label>
            <q-item-label caption class="text-slate-500">{{ link.caption }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
      
      <div class="absolute-bottom p-4 border-t border-slate-800">
        <div class="text-xs text-slate-500 mb-2">Estado del Sistema</div>
        <div class="flex items-center gap-2 text-green-500 text-sm font-bold">
          <div class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
          Online
        </div>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';

// Definimos la interfaz para TypeScript (Punto extra en entrevista)
interface LinkItem {
  title: string;
  caption: string;
  icon: string;
  link?: string;
}

const linksList: LinkItem[] = [
  {
    title: 'Dashboard',
    caption: 'Vista General',
    icon: 'dashboard',
    link: '/'
  },
  {
    title: 'Flota en Vivo',
    caption: 'Mapa y GPS',
    icon: 'map',
    link: '#'
  },
  {
    title: 'Analítica H2',
    caption: 'Consumo Energía',
    icon: 'bar_chart',
    link: '#'
  },
  {
    title: 'Reportes',
    caption: 'I+D+i Docs',
    icon: 'folder_open',
    link: '#'
  }
];

const leftDrawerOpen = ref(false);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>