<template>
  <v-app>
    <v-app-bar app color="primary">
      <v-app-bar-title>My Todo List</v-app-bar-title>
      <v-btn to="/">Home</v-btn>
      <v-btn to="/add-todo">Add Todo</v-btn>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts">
export default {
  name: "App",

  data() {
    return {};
  },
};
</script>
