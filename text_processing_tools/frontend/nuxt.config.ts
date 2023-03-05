import vuetify from 'vite-plugin-vuetify';

export default defineNuxtConfig({
  css: ['vuetify/styles'],
  build: {
    transpile: ['vuetify'],
  },
  modules: [
    async (options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', config => {
        if (config && config.plugins) {
          config.plugins.push(vuetify())
        }
      })
    }
  ],
  ssr: false,
})
