<template>
  <div id="content">
    <v-card id="empty-warning" v-if="!todos" width="400">
      <v-card-item>
        <v-card-title>Your Todo list is empty!</v-card-title>
        <v-card-subtitle>Click below to add some...</v-card-subtitle>
      </v-card-item>
      <v-card-actions>
        <v-btn to="/add-todo" variant="elevated" color="success"
          >Add Todo</v-btn
        >
      </v-card-actions>
    </v-card>
    <div>
      <v-card
        v-for="todo in todos"
        :key="todo.id"
        class="todo-card"
        width="400"
      >
        <v-card-title>
          {{ todo.title }}
        </v-card-title>
        <v-card-text>
          {{ todo.description }}
        </v-card-text>
        <v-card-actions>
          <v-btn
            size="small"
            variant="elevated"
            color="success"
            :to="'/edit-todo/' + todo.id"
            >Edit</v-btn
          >
          <v-btn
            size="small"
            variant="elevated"
            color="error"
            @click="deleteTodo(todo.id)"
            >Delete</v-btn
          >
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  computed: {
    todos() {
      return this.$store.state.todos;
    },
  },
  methods: {
    ...mapActions(["getAllTodos"]),
    deleteTodo(id) {
      fetch("http://localhost:5000/api/todo/" + id, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      }).catch((error) => {
        console.log(error);
      });
      // delete item from cached store as well
      for (const idx in this.todos) {
        if (this.todos[idx].id == id) {
          this.todos.splice(idx, 1);
          break;
        }
      }
    },
  },
  mounted() {
    this.getAllTodos();
  },
};
</script>

<style scoped>
#empty-warning .v-btn {
  margin: 0 2rem 1rem;
}

.todo-card {
  margin-bottom: 2rem;
}

#content {
  display: flex;
  justify-content: center;
  padding: 2rem;
}
</style>
