<template>
  <v-form @submit.prevent="newTodo" id="newTodoForm">
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
      <v-btn type="submit" color="success" form="newTodoForm">Add Todo</v-btn>
      <v-btn color="error" to="/">Cancel</v-btn>
    </div>
  </v-form>
</template>

<script>
import router from "@/router";

export default {
  data() {
    return {
      title: "",
      description: "",
    };
  },
  methods: {
    newTodo() {
      fetch("http://localhost:5000/api/todo", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: this.title,
          description: this.description,
        }),
      })
        .then(() => {
          router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });
    },
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
