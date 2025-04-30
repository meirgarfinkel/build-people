document.addEventListener("DOMContentLoaded", () => {
    // Theme Toggle
    const toggleButton = document.getElementById("theme-toggle");
    const htmlElement = document.documentElement;
    const currentTheme = localStorage.getItem("theme");
    if (currentTheme) htmlElement.classList.add(currentTheme);

    if (toggleButton) {
        toggleButton.addEventListener("click", () => {
            const isDark = htmlElement.classList.contains("dark");
            htmlElement.classList.toggle("dark", !isDark);
            localStorage.setItem("theme", isDark ? "light" : "dark");
        });
    }

    // Mobile Menu Toggle
    const mobileMenuButton = document.getElementById("mobileMenuButton");
    const mobileMenu = document.getElementById("mobileMenu");
    const closeMenu = document.getElementById("closeMenu");

    if (mobileMenuButton && mobileMenu && closeMenu) {
        mobileMenuButton.addEventListener("click", () => mobileMenu.classList.remove("hidden"));
        closeMenu.addEventListener("click", () => mobileMenu.classList.add("hidden"));
        mobileMenu.addEventListener("click", (e) => {
            if (!e.target.closest(".max-w-xs")) mobileMenu.classList.add("hidden");
        });
    }

    // Initial Auto-expand Textareas
    document.querySelectorAll("textarea").forEach((textarea) => {
        textarea.setAttribute("rows", 1);
        textarea.style.height = "auto";
        textarea.style.overflowY = "hidden";
        textarea.style.height = textarea.scrollHeight + "px";
    });

    // Floating Message Fade
    setTimeout(() => {
        const messagesContainer = document.getElementById("floating-messages");
        if (messagesContainer) {
            messagesContainer.style.opacity = "0";
            setTimeout(() => messagesContainer.remove(), 500);
        }
    }, 5000);
});

// Auto-expand Textareas on Input
document.addEventListener("input", (e) => {
    if (e.target.tagName.toLowerCase() !== "textarea") return;
    e.target.setAttribute("rows", 1);
    e.target.style.height = "auto";
    e.target.style.overflowY = "hidden";
    e.target.style.height = e.target.scrollHeight + "px";
});

// HTMX-Aware Enhancements
htmx.onLoad((content) => {
    // Show Bootstrap Toasts
    const toasts = content.querySelectorAll(".toast");
    toasts.forEach((toastEl) => {
        const toastInstance = bootstrap.Toast.getOrCreateInstance(toastEl);
        toastInstance.show();
    });

    // Auto-expand HTMX-loaded Textareas
    content.querySelectorAll("textarea").forEach((textarea) => {
        textarea.setAttribute("rows", 1);
        textarea.style.height = "auto";
        textarea.style.overflowY = "hidden";
        textarea.style.height = textarea.scrollHeight + "px";
    });
});

// Hourly Page Refresh
function scheduleHourlyPageRefresh() {
    const now = new Date();
    const delay = ((60 - now.getMinutes()) * 60 - now.getSeconds()) * 1000;
    setTimeout(() => location.reload(), delay);
}
scheduleHourlyPageRefresh();

// Alpine.js Code Viewer Component
document.addEventListener("alpine:init", () => {
    Alpine.data("codeViewer", (defaultFile) => ({
        file: defaultFile,
        codeContent: "Loading...",
        syntaxClass: "python",

        loadCode() {
            this.syntaxClass = this.getSyntaxClass(this.file);
            fetch(this.file)
                .then((r) => r.text())
                .then((data) => {
                    this.codeContent = data;
                    this.$nextTick(() => {
                        if (window.Prism) Prism.highlightElement(this.$refs.codeBlock);
                    });
                })
                .catch((err) => {
                    this.codeContent = "Failed to load file.";
                    console.error("Error fetching file:", err);
                });
        },

        getSyntaxClass(filePath) {
            const ext = filePath.split(".").pop().toLowerCase();
            return ext === "py" ? "python" : ext === "html" ? "django" : "plaintext";
        },
    }));
});
