import { createStore } from 'vuex';
import createPersistentState from 'vuex-persistedstate';

export default createStore({
  state() {
    return {
      // data = 'something';
    };
  },
  getters: {},
  mutations: {},
  plugins: [
    createPersistentState({
      getState: (key) => JSON.parse(localStorage.getItem(key)),
      setState: (key, state) => localStorage.setItem(key, JSON.stringify(state)),
    }),
  ],
});
