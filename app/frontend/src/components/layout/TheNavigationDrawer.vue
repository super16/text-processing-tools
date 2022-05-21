<template>
  <v-navigation-drawer
    app
    clipped
    flat
    expand-on-hover
    width="400"
  >
    <v-list-item>
        <ListItemContent>
          <span class="font-weight-bold">
            List of corpora
          </span>
        </ListItemContent>
      <ListItemAction
        :action="toggleAddModal"
        :icon="plusIcon"
        tooltip="Add new corpus"
      />
      <ListItemAction
        :action="toggleEditable"
        :icon="editIcon"
        tooltip="Toggle edit"
      />
    </v-list-item>
    <v-list
      v-if="corpora.length > 0"
      nav
    >
      <v-list-group
        v-for="corpus in corpora"
        :key="corpus.id"
        no-action
        sub-group
      >
        <template v-slot:activator>
          <ListItemContent>
            {{ corpus.title }}
          </ListItemContent>
          <ListItemAction
            v-if="editable"
            :action="toggleEditModal"
            :icon="editIcon"
            small
            tooltip="Edit corpus"
            @click.native="updateCorpusToEdit(corpus)"
          />
          <ListItemAction
            v-if="editable"
            :action="toggleDeleteModal"
            color="red"
            :icon="closeIcon"
            small
            tooltip="Delete corpus"
            @click.native="updateCorpusToDelete(corpus)"
          />
        </template>
      </v-list-group>
    </v-list>
    <v-list
      v-else
      dense
      nav
    >
      <v-list-item>
        <ListItemContent>
          <span class="font-weight-light">
            No corpora yet
          </span>
        </ListItemContent>
      </v-list-item>
    </v-list>
    <v-divider />
    <Modal
      :dialog="showAddModal"
      :width="500"
    >
      <AddCorpus @close="toggleAddModal" />
    </Modal>
    <Modal
      :dialog="showEditModal"
      :width="500"
    >
      <EditCorpus
        :corpus="corpusToEdit"
        @close="toggleEditModal"
      />
    </Modal>
    <Modal
      :dialog="showDeleteModal"
      :width="500"
    >
      <DeleteCorpus
        :corpus="corpusToDelete"
        @close="toggleDeleteModal"
      />
    </Modal>
  </v-navigation-drawer>
</template>

<script>
import AddCorpus from '@/components/modals/AddCorpus.vue';
import DeleteCorpus from '@/components/modals/DeleteCorpus.vue';
import EditCorpus from '@/components/modals/EditCorpus.vue';
import ListItemAction from '@/components/ui/ListItemAction.vue';
import ListItemContent from '@/components/ui/ListItemContent.vue';
import Modal from '@/components/ui/Modal.vue';

import { mdiPlus, mdiPencil, mdiClose } from '@mdi/js';
import { mapState, mapActions } from 'vuex';

export default {
  name: 'TheNavigationDrawer',
  data() {
    return {
      closeIcon: mdiClose,
      corpusToDelete: {},
      corpusToEdit: {},
      editable: false,
      editIcon: mdiPencil,
      plusIcon: mdiPlus,
      showAddModal: false,
      showDeleteModal: false,
      showEditModal: false,
    };
  },
  components: {
    AddCorpus,
    DeleteCorpus,
    EditCorpus,
    ListItemAction,
    ListItemContent,
    Modal,
  },
  computed: mapState({
    corpora: (state) => state.corpora.corporaData,
  }),
  created() {
    this.loadCorpora();
  },
  methods: {
    ...mapActions('corpora', ['loadCorpora']),
    toggleAddModal() {
      this.showAddModal = !this.showAddModal;
    },
    toggleDeleteModal() {
      this.showDeleteModal = !this.showDeleteModal;
    },
    toggleEditable() {
      this.editable = !this.editable;
    },
    toggleEditModal() {
      this.showEditModal = !this.showEditModal;
    },
    updateCorpusToDelete(corpus) {
      this.corpusToDelete = corpus;
    },
    updateCorpusToEdit(corpus) {
      this.corpusToEdit = corpus;
    },
  },
};
</script>
