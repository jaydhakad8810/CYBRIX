/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}", "./components/**/*.{js,jsx}", "./pages/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#081120",
        panel: "#0f172a",
        accent: "#22c55e",
        soft: "#94a3b8",
      },
    },
  },
  plugins: [],
};
