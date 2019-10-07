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
                baseURL: 'https://favqs.com/api/',
                url: 'quotes',
                params: {
                    filter: userInput,
                    type: 'author',
                    pageNumber: page,
                },
                headers: {
                    Authorization: 'Token token="3349554fa3d88cf6a1eaa9f75482ac37"'
                },
            })
            .then(function(response) {
                console.log(response.data)
                let quotesList = response.data.quotes;
                quote.innerHTML = `<h1>Quotes by ${specificAuthor.value}`;
                for (let i = 0; i < quotesList.length; i++) {
                    let resultsHTML = `<p>
                    <li>${quotesList[i].body}</li>
                    </p>`
    
                    quote.innerHTML += resultsHTML;
                }
            })
        }
    },

    computed: {

    }

})