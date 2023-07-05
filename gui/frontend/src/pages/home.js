import { createApp } from 'vue';
import store from '@/store';
import Home from './HomeApp.vue';

const ziplineHomeApp = createApp(Home);
ziplineHomeApp.config.globalProperties.window = window;
ziplineHomeApp.use(store).mount('#app');
