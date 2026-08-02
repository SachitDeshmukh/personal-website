// ======================================================
// Article Template JavaScript
// ======================================================

// ---------- Theme Toggle ----------
const themeToggle = document.getElementById("themeToggle");
const root = document.documentElement;

// Load previously selected theme
const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {
    root.classList.add("dark");
}

// Toggle theme
themeToggle.addEventListener("click", () => {
    root.classList.toggle("dark");

    if (root.classList.contains("dark")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
});