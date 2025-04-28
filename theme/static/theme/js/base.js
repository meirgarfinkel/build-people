import "../../../static_src/node_modules/preline/dist/preline.js";

// HTMX Bootstrap Toast Support
htmx.onLoad(function (content) {
    var toasts = content.querySelectorAll(".toast");
    if (toasts.length > 0) {
        console.log("Initializing toasts:", toasts);
        toasts.forEach(function (toastEl) {
            var toastInstance = bootstrap.Toast.getOrCreateInstance(toastEl);
            toastInstance.show();
        });
    }
});

// Hourly Page Refresh Alert
function scheduleHourlyPageRefresh() {
    const now = new Date();
    const minutesUntilNextHour = 60 - now.getMinutes();
    const secondsUntilNextHour = minutesUntilNextHour * 60 - now.getSeconds();

    setTimeout(() => {
        location.reload(); // Auto-refresh the page
    }, secondsUntilNextHour * 1000);
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
                .then((response) => response.text())
                .then((data) => {
                    this.codeContent = data;
                    this.$nextTick(() => {
                        if (window.Prism) {
                            Prism.highlightElement(this.$refs.codeBlock);
                        }
                    });
                })
                .catch((error) => {
                    this.codeContent = "Failed to load file.";
                    console.error("Error fetching file:", error);
                });
        },

        getSyntaxClass(filePath) {
            const extension = filePath.split(".").pop().toLowerCase();
            switch (extension) {
                case "py": return "python";
                case "html": return "django";
                default: return "plaintext";
            }
        },
    }));
});

// Auto-expand textareas on input
document.addEventListener("input", function (e) {
    if (e.target.tagName.toLowerCase() !== "textarea") return;
    e.target.setAttribute("rows", 1);
    e.target.style.height = "auto";
    e.target.style.overflowY = "hidden";
    e.target.style.height = e.target.scrollHeight + "px";
});

// Auto-expand textareas on input
document.addEventListener("DOMContentLoaded", () => {
    // Initialize all visible textareas to auto-expand from the start
    document.querySelectorAll("textarea").forEach((textarea) => {
        textarea.setAttribute("rows", 1);
        textarea.style.height = "auto";
        textarea.style.overflowY = "hidden";
        textarea.style.height = textarea.scrollHeight + "px";
    });
});

// Auto-expand textareas on input
htmx.onLoad(function (content) {
    content.querySelectorAll("textarea").forEach((textarea) => {
        textarea.setAttribute("rows", 1);
        textarea.style.height = "auto";
        textarea.style.overflowY = "hidden";
        textarea.style.height = textarea.scrollHeight + "px";
    });
});

// Fade out floating messages after 2s (HTMX safe)
document.addEventListener("DOMContentLoaded", () => {
    setTimeout(function () {
        const messagesContainer = document.getElementById("floating-messages");
        if (messagesContainer) {
            messagesContainer.style.opacity = "0";
            setTimeout(() => messagesContainer.remove(), 500);
        }
    }, 5000);
});

// Mobile Menu Toggle
document.addEventListener("DOMContentLoaded", () => {
    const mobileMenuButton = document.getElementById("mobileMenuButton");
    const mobileMenu = document.getElementById("mobileMenu");
    const closeMenu = document.getElementById("closeMenu");

    // Ensure elements exist before adding event listeners
    if (mobileMenuButton && mobileMenu && closeMenu) {
        mobileMenuButton.addEventListener("click", () => {
            mobileMenu.classList.remove("hidden");
        });

        closeMenu.addEventListener("click", () => {
            mobileMenu.classList.add("hidden");
        });

        // Close modal when clicking outside
        mobileMenu.addEventListener("click", (e) => {
            if (!e.target.closest(".max-w-xs")) {
                mobileMenu.classList.add("hidden");
            }
        });
    }
});
