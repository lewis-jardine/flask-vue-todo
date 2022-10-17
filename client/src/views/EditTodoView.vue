<template>
  <v-form @submit.prevent="newTodo" id="editTodoForm">
    <v-text-field
      v-model="title"
      :counter="100"
      label="Title"
      required
    ></v-text-field>
    <v-textarea
      v-model="description"
      :counter="400"
      label="Description"
      auto-grow
      :rows="3"
    ></v-textarea>
    <div id="buttons">
      <v-btn type="submit" color="success" form="editTodoForm">Edit Todo</v-btn>
      <v-btn color="error" to="/">Cancel</v-btn>
    </div>
  </v-form>
</template>

<script>
import router from "@/router";

export default {
  data() {
    return {
      id: this.$route.params.id,
      title: "",
      description: "",
    };
  },
  methods: {
    newTodo() {
      fetch("http://localhost:5000/api/todo/" + this.id, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify({
          title: this.title,
          description: this.description,
        }),
      }).then(() => {
        router.push("/");
      });
    },
    getTodo(id) {
      fetch("http://localhost:5000/api/todo/" + id)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.title = data.title;
          this.description = data.description;
        });
    },
  },
  created() {
    this.getTodo(this.id);
  },
};
</script>

<style scoped>
.v-form {
  width: 400px;
  margin: 2rem auto;
}

#buttons {
  display: flex;
  justify-content: space-evenly;
}
</style>
