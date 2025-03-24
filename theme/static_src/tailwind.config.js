const path = require("path")

module.exports = {
    content: [
        path.join(__dirname, "..", "templates/**/*.html"), // Project-level templates
        path.join(__dirname, "../../**/templates/**/*.html"), // App-specific templates
        path.join(__dirname, "theme/templates/**/*.html"), // Tailwind theme templates
        path.join(__dirname, "theme/static_src/**/*.js"), // JavaScript files
    ],
    theme: {
        extend: {},
    },
    plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography"), require("@tailwindcss/aspect-ratio")],
    output: path.join(__dirname, "theme/static/css/dist/styles.css"),
}
