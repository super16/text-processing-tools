<template>
  <v-card>
    <v-card-title class="white--text secondary">
      Edit corpus
    </v-card-title>
    <v-container>
      <v-text-field
        v-model="corpus.title"
        clearable
        hide-details
        label="Title"
        outlined
        placeholder="Enter corpus title"
      />
    <v-card-actions>
      <v-spacer />
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
        @click="renameCorpus(corpus)"
      >
        Edit
      </v-btn>
      </v-card-actions>
    </v-container>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  props: {
    corpus: Object,
  },
  methods: {
    ...mapActions('corpora', ['editCorpus']),
    renameCorpus(corpus) {
      this.editCorpus({ id: corpus.id, title: corpus.title });
      this.$emit('close');
    },
  },
};
</script>
