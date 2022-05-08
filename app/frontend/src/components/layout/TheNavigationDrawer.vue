<template>
  <v-navigation-drawer app clipped flat expand-on-hover width="400">
    <v-list-item>
        <ListItemContent>
          <span class="font-weight-bold">List of corpora</span>
        </ListItemContent>
      <ListItemAction :icon="plusIcon" :action="toggleAddModalDialog" tooltip="Add new corpus"/>
      <ListItemAction :icon="editIcon" :action="toggleEditable" tooltip="Toggle edit"/>
    </v-list-item>
    <v-list v-if="corpora.length > 0" nav>
      <v-list-group no-action sub-group v-for="corpus in corpora" :key="corpus.id">
        <template v-slot:activator>
          <ListItemContent>
            {{ corpus.title }}
          </ListItemContent>
          <ListItemAction
            v-if="editable" small :icon="editIcon"
            :action="editCorpus" tooltip="Edit corpus"
            @click.native="updateCorpusToEdit(corpus)" />
          <ListItemAction v-if="editable" small :icon="closeIcon" disabled :action="toggleEditable"
            color="red" tooltip="Delete corpus"/>
        </template>
      </v-list-group>
    </v-list>
    <v-list v-else dense nav>
      <v-list-item>
        <ListItemContent>
          <span class="font-weight-light">No corpora yet</span>
        </ListItemContent>
      </v-list-item>
    </v-list>
    <v-divider />
    <Modal :dialog="modalAddDialog" :width="500">
      <AddCorpus :toggle="toggleAddModalDialog"/>
    </Modal>
    <Modal :dialog="editModalDialog" :width="500">
      <EditCorpus :toggle="editCorpus" :corpus="corpusToEdit" />
    </Modal>
  </v-navigation-drawer>
</template>

<script>
import EditCorpus from '@/components/modals/EditCorpus.vue';
import ListItemAction from '@/components/ui/ListItemAction.vue';
import ListItemContent from '@/components/ui/ListItemContent.vue';
import Modal from '@/components/ui/Modal.vue';
import AddCorpus from '@/components/modals/AddCorpus.vue';
import { mdiPlus, mdiPencil, mdiClose } from '@mdi/js';
import { mapState, mapActions } from 'vuex';

export default {
  name: 'TheNavigationDrawer',
  data() {
    return {
      plusIcon: mdiPlus,
      editIcon: mdiPencil,
      corpusToEdit: {},
      closeIcon: mdiClose,
      editable: false,
      editModalDialog: false,
      modalAddDialog: false,
    };
  },
  components: {
    EditCorpus,
    ListItemAction,
    ListItemContent,
    Modal,
    AddCorpus,
  },
  computed: mapState({
    corpora: (state) => state.corpora.corporaData,
  }),
  methods: {
    ...mapActions('corpora', ['loadCorpora']),
    updateCorpusToEdit(corpus) {
      this.corpusToEdit = corpus;
    },
    editCorpus() {
      this.editModalDialog = !this.editModalDialog;
    },
    toggleEditable() {
      this.editable = !this.editable;
    },
    toggleAddModalDialog() {
      this.modalAddDialog = !this.modalAddDialog;
    },
  },
  created() {
    this.loadCorpora();
  },
};
</script>
