<template>
  <v-app>
    <v-app-bar flat app dark clipped-left color="primary">
      <v-toolbar-title>Text Processing Tools</v-toolbar-title>
    </v-app-bar>
    <TheNavigationDrawer/>
    <v-main>
      <router-view />
    </v-main>
    <v-snackbar
      :value="alertState"
      right
      bottom
      dark
      app
      color="primary"
    >
      {{ alertText }}
    </v-snackbar>
    <v-footer app />
  </v-app>
</template>

<script>
import TheNavigationDrawer from '@/components/layout/TheNavigationDrawer.vue';
import { mapGetters, mapState } from 'vuex';

export default {
  name: 'App',
  components: { TheNavigationDrawer },
  computed: {
    ...mapGetters('alert', ['alertState']),
    ...mapState({
      alertText: (state) => state.alert.text,
    }),
  },
};
</script>
