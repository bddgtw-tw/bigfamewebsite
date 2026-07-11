/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.html',
    './tw/**/*.html',
    './en/**/*.html',
    './jp/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        display: ['"Shippori Mincho"', 'YuMincho', 'serif'],
        body: ['Outfit', '"Noto Sans TC"', '"Noto Sans JP"', 'sans-serif'],
      },
      colors: {
        ink: {
          DEFAULT: '#111111',
          light: '#555555',
          muted: '#999999',
        },
        paper: {
          DEFAULT: '#ffffff',
          warm: '#f8f7f4',
        },
        gold: {
          DEFAULT: '#9e8561',
        },
        dark: {
          DEFAULT: '#0f0f0f',
          accent: '#151515',
        },
        border: {
          DEFAULT: '#e5e5e5',
          dark: '#222222',
        },
      },
      letterSpacing: {
        display: '0.02em',
        wide: '0.15em',
        wider: '0.25em',
      },
      maxWidth: {
        container: '1200px',
      },
      spacing: {
        section: '80px',
        'section-sm': '60px',
        'section-lg': '100px',
      },
      borderRadius: {
        none: '0px',
      },
      fontSize: {
        hero: ['3.25rem', { lineHeight: '1.15', letterSpacing: '-0.03em' }],
        'section-title': ['2.25rem', { lineHeight: '1.25', letterSpacing: '0.02em' }],
      },
      transitionTimingFunction: {
        smooth: 'cubic-bezier(0.16, 1, 0.3, 1)',
      },
    },
  },
  plugins: [],
}