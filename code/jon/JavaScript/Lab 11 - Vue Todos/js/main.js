new Vue({
    el: '#app',
    data: {
        message: `My To-Do List`,
        todos: [],
        newTodo: {
            text: '',
            isComplete: false,
        },
    },
        
    methods: {
        add: function () {
            this.todos.push({text: this.newTodo.text, isComplete: this.newTodo.isComplete});
            newTodo.text = '';
        },
        remove: function (index) {
            this.todos.splice(index, 1);
        },
    },
}) 