# 🚛 GreenRoute Analytics
### Plataforma de Optimización y Telemetría para Transporte de Hidrógeno Verde

![Java](https://img.shields.io/badge/Java-17%2B-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-3.x-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-Realtime-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)

## 📖 Resumen del Proyecto

**GreenRoute Analytics** es un sistema distribuido diseñado para la gestión y monitoreo en tiempo real de flotas de transporte impulsadas por Hidrógeno Verde. El proyecto simula escenarios de logística, calcula el consumo energético basado en física y visualiza la telemetría en un dashboard interactivo.

Este proyecto integra una arquitectura híbrida con un **Backend transaccional** (Java/Spring Boot) para la gestión administrativa y un **Microservicio de Simulación** (Python) que alimenta datos de sensores IoT en tiempo real a la nube (Firebase Firestore).

## 🏗️ Arquitectura del Sistema

El sistema sigue una arquitectura de microservicios simplificada y orientada a eventos:

```mermaid
graph TD
    User[Usuario / Operador] -->|HTTPS| Frontend(Vue.js + Quasar)
    
    subgraph "Backend Core (Transaccional)"
        Frontend -->|REST API| SpringBoot[Spring Boot Service]
        SpringBoot -->|JPA/Hibernate| Postgres[(PostgreSQL DB)]
    end
    
    subgraph "Data Science & Simulation"
        Python[Python Simulation Script] -->|OSRM API| Routing[Open Source Routing Machine]
        Python -->|Telemetría JSON| Firebase[(Firebase Firestore)]
    end
    
    subgraph "Real-time Sync"
        Firebase -.->|WebSockets / Snapshot| Frontend
    end
