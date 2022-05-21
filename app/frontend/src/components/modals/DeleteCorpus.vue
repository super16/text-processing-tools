<template>
  <v-card>
    <v-card-title class="white--text secondary">
      Delete corpus
    </v-card-title>
    <v-card-text class="body-1 mt-4">
      Are you sure to delete
      <span class="font-weight-bold">{{ corpus.title }}</span>?
    </v-card-text>
    <v-container>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        color="red darken-1"
        oultined
        text
        @click="$emit('close')"
      >
        Cancel
      </v-btn>
      <v-btn
        color="green darken-1"
        text
        @click="deleteItem"
      >
        Delete
      </v-btn>
      </v-card-actions>
    </v-container>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'DeleteCorpus',
  props: {
    corpus: Object,
  },
  methods: {
    ...mapActions('corpora', ['deleteCorpus']),
    deleteItem() {
      this.deleteCorpus({ id: this.corpus.id });
      this.$emit('close');
    },
  },
};
</script>
