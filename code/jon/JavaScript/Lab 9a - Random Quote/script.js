const quoteButton = document.getElementById('button');
const quote = document.getElementById('quote');

quoteButton.addEventListener('click', function () {
    axios({
            method: 'get',
            url: 'https://favqs.com/api/qotd',
            headers: {
                Authorization: 'Token token=""'
            }
        })
        .then(function (response) {
            console.log(response);

            let result = `<p><h4>${response.data.quote.body}</h4></p>
            <p><em>By: ${response.data.quote.author}</em></p>`;

            quote.innerHTML = result;
        })

});