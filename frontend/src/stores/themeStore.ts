
import { defineStore } from 'pinia';

export const useThemeStore = defineStore('themeStore', {
  state: () => ({
    currentTheme: localStorage.getItem('theme') || 'aura-light-cyan',
  }),
  actions: {
    setTheme(newTheme: string) {
      this.currentTheme = newTheme;
      localStorage.setItem('theme', newTheme);
    },
  },
});
