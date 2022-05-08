export default {
  namespaced: true,
  state: () => ({
    show: false,
    text: '',
    timeout: 5000,
  }),
  getters: {
    alertState(state) {
      return state.show;
    },
  },
  mutations: {
    updateAlertText(state, text) {
      state.text = text;
    },
    toggleAlert(state) {
      state.show = !state.show;
    },
  },
  actions: {
    callAlert(context, text) {
      context.commit('updateAlertText', text);
      context.commit('toggleAlert');
      setTimeout(() => {
        context.commit('toggleAlert');
      }, context.state.timeout);
    },
  },
};
