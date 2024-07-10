function capitalize(e: KeyboardEvent) {
  const target = e.target as HTMLInputElement;
  const start = target.selectionStart || 0;
  target.value = target.value.toUpperCase();
  target.setSelectionRange(start, start);
}


export default {
  mounted(el: HTMLElement) {
    el.addEventListener('keypress', capitalize);
  },
  unmounted(el: HTMLElement) {
    el.removeEventListener('keypress', capitalize);
  },
};
