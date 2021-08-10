import axios from 'axios';

export default {
  namespaced: true,
  state: () => ({
    corporaData: [],
    lastAddedCorpus: '',
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
  },
  actions: {
    async loadCorpora(context) {
      await axios.get('corpora').then(
        (response) => (
          context.commit('updateCorporaData', response.data.corpora)
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
      );
    },
  },
};
