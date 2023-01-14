/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["./templates/**/*.{html,js}"],
  theme: {
    screens: {
      sm: "480px",
      md: "768px",
      lg: "976px",
      xl: "1440px",
    },
    colors: {
      lightviolet: "#CDB4DB",
      lightmagenta: "#FFC8DD",
      lightpink: "#FFAFCC",
      lightblue: "#BDE0FE",
      blue: "#A2D2FF",
      white: "#FFFFFF",
    },
    extend: {},
  },
  plugins: [],
};
