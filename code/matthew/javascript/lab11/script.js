new Vue({
    el: '#app',
    data: {
        newTodo: {
            task: '',
            completed: false,
        },
        todos: [
            { task: "Finish Lab 10", completed: false },
            { task: "Prepare a project for Stephen", completed: false },
            { task: "Contact Matt re: meeting location/time for Wed.", completed: false },
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