<template>
  <v-list-item-action>
    <v-tooltip bottom color="blue-grey lighten-3">
      <template v-slot:activator="{ on, attrs }">
        <v-btn icon small :color="color"
          :disabled="disabled" @click="action" v-bind="attrs" v-on="on">
          <v-icon :small="small" :color="color">{{ icon }}</v-icon>
        </v-btn>
      </template>
      <span>{{ tooltip }}</span>
    </v-tooltip>
  </v-list-item-action>
</template>

<script>
export default {
  props: {
    action: Function,
    color: {
      type: String,
    },
    disabled: Boolean,
    icon: String,
    small: Boolean,
    tooltip: String,
  },
};
</script>
