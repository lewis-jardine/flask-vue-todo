import { createStore } from "vuex";

const store = createStore({
  state() {
    return {
      todos: [],
    };
  },
  mutations: {
    // eslint-disable-next-line
    setTodos(state: any, todos) {
      state.todos = todos;
    },
  },
  actions: {
    async getAllTodos(context) {
      try {
        const response = await fetch("http://localhost:5000/api/todo");
        const data = await response.json();
        context.commit("setTodos", data);
      } catch (error) {
        return console.error(error);
      }
    },
  },
  getters: {
    todos(state) {
      return state.todos;
    },
  },
});

export default store;
