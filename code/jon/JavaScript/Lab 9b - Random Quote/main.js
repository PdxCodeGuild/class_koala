let pageNumber = 1;

const quoteButton = document.getElementById('button');
const quote = document.getElementById('quote');
const specificButton = document.getElementById('specific')
let specificAuthor = document.getElementById('author');
let quotesby = document.getElementById('quotes-by');
let pages = document.getElementById('pages');
let nextPageButton = document.getElementById('nextPageButton');
let previousPageButton = document.getElementById('previousPageButton');
let nextPageDiv = document.getElementById('nextPageDiv');
let previousPageDiv = document.getElementById('previousPageDiv');
let previousAndNextPageDiv = document.getElementById('previousAndNextDiv');


//Random Quotes

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

//Specific Author

function getQuotes() {
    axios({
            method: 'get',
            baseURL: 'https://favqs.com/api',
            url: `quotes/`,
            params: {
                filter: specificAuthor.value,
                type: 'author',
                page: pageNumber,
            },
            headers: {
                Authorization: 'Token token="3349554fa3d88cf6a1eaa9f75482ac37"'
            },
        })
        .then(function (response) {
            let quotesList = response.data.quotes;
            quote.innerHTML = `<h1>Quotes by ${specificAuthor.value}`;
            for (let i = 0; i < quotesList.length; i++) {
                let resultsHTML = `<p>
                <li>${quotesList[i].body}</li>
                </p>`

                quote.innerHTML += resultsHTML;
            }
            if (response.data.last_page == true) {
                nextPageButton.style.display = 'none';
            }
            if (response.data.last_page == false && response.data.page == 1) {
                previousPageButton. style.display = 'none';
            }
            if (response.data.last_page == false && response.data.page > 1) {
                nextPageButton.style.display = 'inline';
                previousPageButton.style.display = 'inline';
            }
        })
}

specificButton.addEventListener('click', getQuotes);

function checkPageNumber() {
    if (pageNumber === 1) {
        previousPageButton.style.display = 'none';
    }
    }

function nextPage () {
    pageNumber += 1;
    getQuotes();
    checkPageNumber()
}

function previousPage() {
    pageNumber -= 1;
    getQuotes();
    checkPageNumber();
}

specificButton.addEventListener('click', function() {
    getQuotes();
})

nextPageButton.addEventListener('click', function () {
    nextPage();
    getQuotes();
})

previousPageButton.addEventListener('click', function() {
    previousPage();
    getQuotes();
})





