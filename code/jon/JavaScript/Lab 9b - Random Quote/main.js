const quoteButton = document.getElementById('button');
const quote = document.getElementById('quote');
const specificButton = document.getElementById('specific')
let specificAuthor = document.getElementById('author');
let quotesby = document.getElementById('quotes-by');


quoteButton.addEventListener('click', function () {
    axios({
            method: 'get',
            url: 'https://favqs.com/api/qotd',
            headers: {
                Authorization: 'Token token=""'
            }
        })
        .then(function (response) {

            console.log(response.data);
            quotesby.style.display = 'none';


            let result = `<p><h4>${response.data.quote.body}</h4></p>
            <p><em>By: ${response.data.quote.author}</em></p>`;

            quote.innerHTML = result;
        })

});

specificButton.addEventListener('click', function () {
    axios({
            method: 'get',
            url: `https://favqs.com/api/quotes/?filter=${specificAuthor.value}&type=author`,
            headers: {
                Authorization: 'Token token=""'
            },
        })
        .then(function (response) {
            console.log(response.data.quotes);
            let quotesList = response.data;
            let results = [];

            console.log(`Inside: ${quotesList}`);
            function clearBox() {
                results = [];
                quote.innerHTML = '';
                quotesby.style.display = 'inline';
            }
            clearBox();

            for (let i = 0; i < quotesList.length; i++) {
                results.push(quotesList[i].body);
            }
            quotesby.innerHTML = `Quotes by: ${specificAuthor.value}` //displays name of author
            for (let j = 0; j < results.length; j++) {
                quote.innerHTML += `<li>${results[j]}</li>`; // displays the quotes by the author
            }
            // console.log(quotesList.last_page.value);
            // specificAuthor.value = '';
        })
        // .then(function(response) {
        //     if (quoteList.last_page)
        // })
});