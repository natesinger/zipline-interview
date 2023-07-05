import { createApp } from 'vue';
import store from '@/store';
import FourOhFour from './404App.vue';

const hab404App = createApp(FourOhFour);
hab404App.config.globalProperties.window = window;
hab404App.use(store).mount('#app');
