Vue.component('previouspage', {
    methods: {
        previouspage: function () {

            if (this.$parent.page === 2) {
                previousbutton.style.display = 'inline';
            } else if (this.$parent.page === 1) {
                previousbutton.style.display = 'none';
            } else if (this.$parent.page > 1) {
                this.$parent.page--;
                this.$parent.search();
            };
        }
    },
    template: `
            <button id="previousbutton" @click='previouspage'>Previous</button>
    `
})

Vue.component('nextpage', {

    methods: {
        nextpage: function () {
            this.$parent.page++;
            this.$parent.search();
        }
    },
    template: `
            <button id="nextbutton" @click='nextpage'>Next</button>
    `
})


new Vue({
    el: '#app',
    data: {
        userInput: null,
        lastPage: '',
        page: 1,
        quotes: [],
        searchby: null,
    },
    methods: {
        search: function () {
            axios({
                    method: 'get',
                    baseURL: 'https://favqs.com/api/',
                    url: 'quotes',
                    params: {
                        filter: this.userInput,
                        type: this.searchby,
                        pageNumber: this.page,
                    },
                    headers: {
                        Authorization: 'Token token="3349554fa3d88cf6a1eaa9f75482ac37"'
                    },
                })
                .then((response) => {
                    this.quotes = response.data.quotes;
                    console.log(this.quotes);
                })
        },
    },
    mounted: function () {
        this.search();
    }

})