<template>
  <v-card>
    <v-card-title class="white--text secondary">
      Add new corpus
    </v-card-title>
    <v-container>
      <v-text-field label="Title" placeholder="Enter corpus title"
        v-model="corpusTitle" outlined clearable hide-details>
      </v-text-field>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="red darken-1" text oultined @click="toggle">
        Cancel
      </v-btn>
      <v-btn color="green darken-1" text @click="addCorpus(corpusTitle)">
        Add
      </v-btn>
      </v-card-actions>
    </v-container>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  props: {
    toggle: Function,
  },
  data() {
    return {
      corpusTitle: '',
    };
  },
  methods: {
    ...mapActions('corpora', ['postCorpus']),
    addCorpus(title) {
      this.postCorpus(title);
      this.corpusTitle = '';
      this.toggle();
    },
  },
};
</script>
