<template>
  <v-dialog v-model="dialog" :width="width" persistent>
    <slot></slot>
  </v-dialog>
</template>

<script>
export default {
  props: {
    dialog: Boolean,
    width: Number,
  },
};
</script>
