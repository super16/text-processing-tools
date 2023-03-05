import { createVuetify } from 'vuetify';

const customDarkTheme = {
  dark: false,
  colors: {
    primary: '#415A77',
    secondary: '#778DA9',
    white: '#FFFFFF',
  },
}

export default defineNuxtPlugin((nuxtApp) => {
  const vuetify = createVuetify({
    theme: {
      defaultTheme: 'customDarkTheme',
      themes: {
        customDarkTheme,
      }
    },
  })
  nuxtApp.vueApp.use(vuetify);
});
