import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

import HomeView from "../views/HomeView.vue";
import AddTodoView from "../views/AddTodoView.vue";
import EditTodoView from "../views/EditTodoView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/add-todo",
    name: "AddTodo",
    component: AddTodoView,
  },
  {
    path: "/edit-todo/:id",
    name: "EditTodo",
    component: EditTodoView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
