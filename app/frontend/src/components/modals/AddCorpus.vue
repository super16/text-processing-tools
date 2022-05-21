<template>
  <v-card>
    <v-card-title class="white--text secondary">
      Add new corpus
    </v-card-title>
    <v-container>
      <v-text-field
        v-model="corpusTitle"
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
        @click="addCorpus(corpusTitle)"
      >
        Add
      </v-btn>
      </v-card-actions>
    </v-container>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';

export default {
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
      this.$emit('close');
    },
  },
};
</script>
