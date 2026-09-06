/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: { 
    extend: {
      colors: {
        space: {
          900: '#050510',
          800: '#0a0a23',
          700: '#0d0d2b',
        }
      },
      fontFamily: {
        space: ['Space Grotesk', 'sans-serif'],
      },
      animation: {
        drift: 'drift 20s ease-in-out infinite',
        twinkle: 'twinkle 2s ease-in-out infinite',
      },
      keyframes: {
        drift: {
          '0%, 100%': { transform: 'translate(0,0)' },
          '50%': { transform: 'translate(20px,-15px)' },
        },
        twinkle: {
          '0%, 100%': { opacity: '0.3' },
          '50%': { opacity: '1' },
        },
      },
    } 
  },
  plugins: [], // ลบ @tailwindcss/typography ออกแล้ว - แก้ Error 500
}
