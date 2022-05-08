import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'mdiSvg',
  },
  theme: {
    themes: {
      light: {
        primary: '#415A77',
        secondary: '#778DA9',
        white: '#FFFFFF',
      },
      dark: {
        primary: '#415A77',
        secondary: '#778DA9',
        white: '#FFFFFF',
      },
    },
  },
});
