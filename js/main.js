/* =====================================================================
   THEME TOGGLE
   Clicking the circular button in the header switches between
   light and dark mode by toggling a "dark" class on <html>.
   All colors respond automatically via the CSS variables in style.css.
   ===================================================================== */

const root = document.documentElement;
const themeToggle = document.getElementById('themeToggle');

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    root.classList.toggle('dark');
  });
}

/* =====================================================================
   HERO ROLE WORD
   Cycles the italic word in the headline ("writer", "developer", ...).
   Edit the "roles" array below to change the words or their order.
   ===================================================================== */

const roles = ['writer', 'developer', 'researcher', 'organizer'];
const roleEl = document.getElementById('roleWord');
let roleIndex = 0;

if (roleEl) {
  setInterval(() => {
    roleIndex = (roleIndex + 1) % roles.length;

    roleEl.style.opacity = 0;
    roleEl.style.transform = 'translateY(6px)';

    setTimeout(() => {
      roleEl.textContent = roles[roleIndex];
      roleEl.style.opacity = 1;
      roleEl.style.transform = 'translateY(0)';
    }, 300);
  }, 2600);
}
