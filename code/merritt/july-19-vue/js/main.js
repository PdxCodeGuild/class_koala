let app = new Vue({
  el: '#app',
  data: {
    message: 'Hello world!',
    titleMessage: 'I typed this',
    exists: true,
    todos: [
      { text: 'Learn JavaScript', isCompleted: false },
      { text: 'Learn Vue', isCompleted: false },
      { text: 'Build something awesome', isCompleted: false }
    ],
    newTodo: {
      text: '',
      isCompleted: false
    },
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('');
    },
    addTodo: function () {
      this.todos.push({ text: this.newTodo.text, isCompleted: this.newTodo.isCompleted});
    },
    removeTodo: function (index) {
      this.todos.splice(index , 1);
    }
  }
});