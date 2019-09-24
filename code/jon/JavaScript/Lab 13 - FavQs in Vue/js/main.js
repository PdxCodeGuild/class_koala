new Vue({
    el: '#app',
    data: {
        userInput: '',
        lastPage: '',
        page: 1,
        quotes: '',
    },
    methods: {
        search: function () {
            axios({
                method: 'post',
                baseURL: 'https://favqs.com/api/'
                url: 'quotes',
                header: {
                    Authorization: 'Token token=""'
                }

            }),
            .then(function(response) {
                console.log(response)
            })
        }
    },
    mounted: function () {
        this.search();
    },

    computed: {

    }

})