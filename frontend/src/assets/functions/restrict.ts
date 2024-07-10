function restrict(e: KeyboardEvent) {
    const char = e.key.toUpperCase(); // Convert typed character to uppercase
  
    // Allow numbers (0-9) and letters (A-F)
    if (!/[0-9A-F]/.test(char)) {
      e.preventDefault(); // Prevent default action for any other key press
    }
  }
  
  export default {
    mounted(el: HTMLElement) {
      el.addEventListener('keydown', restrict);
    },
    unmounted(el: HTMLElement) {
      el.removeEventListener('keydown', restrict);
    },
  };
  
  
  