<template>
  <v-card>
    <v-card-title class="white--text secondary">
      Edit corpus
    </v-card-title>
    <v-container>
      <v-text-field label="Title" placeholder="Enter corpus title"
        v-model="corpus.title" outlined clearable hide-details>
      </v-text-field>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="red darken-1" text oultined @click="toggle">
        Cancel
      </v-btn>
      <v-btn color="green darken-1" text @click="renameCorpus(corpus)">
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
    toggle: Function,
  },
  methods: {
    ...mapActions('corpora', ['editCorpus']),
    renameCorpus(corpus) {
      this.editCorpus({ id: corpus.id, title: corpus.title });
      this.toggle();
    },
  },
};
</script>
