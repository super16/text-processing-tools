import axios from 'axios';

export default {
  namespaced: true,
  state: () => ({
    corporaData: [],
    lastAddedCorpus: '',
    lastDeletedCorpus: '',
  }),
  getters: {
    corporaCount(state) {
      return state.corporaData.length;
    },
  },
  mutations: {
    updateCorporaData(state, corpora) {
      state.corporaData = corpora;
    },
    updateLastAddedCorpus(state, title) {
      state.lastAddedCorpus = title;
    },
    updateLastDeletedCorpus(state, title) {
      state.lastDeletedCorpus = title;
    },
  },
  actions: {
    async loadCorpora(context) {
      await axios.get('corpora').then(
        (response) => (
          context.commit('updateCorporaData', response.data.data)
        ),
      );
    },
    async postCorpus(context, title) {
      context.commit('updateLastAddedCorpus', '');
      return axios.post('corpora', {
        title,
      }).then(
        (response) => {
          context.dispatch('loadCorpora');
          context.commit('updateLastAddedCorpus', response.data.title);
          context.dispatch(
            'alert/callAlert',
            `${context.state.lastAddedCorpus} corpus has been added`,
            { root: true },
          );
        },
      ).catch((error) => {
        context.dispatch(
          'alert/callAlert',
          error.response.data.error,
          { root: true },
        );
      });
    },
    async editCorpus(context, { id, title }) {
      context.commit('updateLastAddedCorpus', '');
      return axios.put(`corpora/${id}`, {
        title,
      }).then(
        (response) => {
          context.dispatch('loadCorpora');
          context.commit('updateLastAddedCorpus', response.data.title);
          context.dispatch(
            'alert/callAlert',
            `Corpus has been renamed to ${context.state.lastAddedCorpus}`,
            { root: true },
          );
        },
      ).catch((error) => {
        context.dispatch('loadCorpora');
        context.dispatch(
          'alert/callAlert',
          error.response.data.error,
          { root: true },
        );
      });
    },
    async deleteCorpus(context, { id }) {
      return axios.delete(`corpora/${id}`, { id })
        .then(
          (response) => {
            context.dispatch('loadCorpora');
            context.commit('updateLastDeletedCorpus', response.data.title);
            context.dispatch(
              'alert/callAlert',
              `Corpus ${context.state.lastDeletedCorpus} has been deleted`,
              { root: true },
            );
          }
        ).catch((error) => {
          context.dispatch('loadCorpora');
          context.dispatch(
            'alert/callAlert',
            error.response.data.error,
            { root: true },
          );
        });
    }
  },
};
