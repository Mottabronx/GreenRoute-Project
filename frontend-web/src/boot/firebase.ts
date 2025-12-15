import { boot } from 'quasar/wrappers';
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';

// Pega aquí TU configuración de Firebase
const firebaseConfig = {
  apiKey: process.env.FIREBASE_API_KEY as string,
  authDomain: "greenroute-analytics.firebaseapp.com",
  projectId: "greenroute-analytics",
  storageBucket: "greenroute-analytics.firebasestorage.app",
  messagingSenderId: "328652087976",
  appId: "1:328652087976:web:1a19bdebb814c99106d89d",
  measurementId: "G-VQM9MFD1MY"
};

// Inicializar Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Exportamos 'db' para usarlo en los componentes
export { db };

export default boot(() => {
  // Esto permite que Quasar sepa que Firebase está listo
});
