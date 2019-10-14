new Vue({
    el: '#app',
    data: {
        newTodo: {
            task: '',
            completed: false,
        },
        todos: [
            { task: "Finish Labs", completed: false },
            { task: "Finish Capstone", completed: false },
        ]
    },
    methods: {
        addItem: function () {
            this.todos.push({ task: this.newTodo.task, completed: this.newTodo.completed });
        },
        removeItem: function (index) {
            this.todos.splice(index, 1);
        },
    },
})
