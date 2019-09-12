///////////// GLOBAL VARIABLES //////////////

let page = 1;

let quoteButton = document.getElementById("quote-button");
let target = document.getElementById("target");
let prevButton = document.getElementById("prevButton");
let nextButton = document.getElementById("nextButton");

///////////// FUNCTIONS //////////////

function getQuotes() {
	axios({
		method: "get",
		baseURL: "https://favqs.com/api/quotes/",
		params: {
			page: page,
			filter: "peace",
		},
		headers: {
			Authorization: 'Token token=""'
		}
	})
	.then(function(response) {
		console.log(response);
		let quotes = response.data.quotes;
		target.innerHTML = "";
		for(let quote of quotes) {			
			let currentQuotes = `
			<div class="mt-4">
				<p>${quote.body}</p>
				<p><a href=${quote.url}>${quote.author}</a></p>
			</div>
			`;
			target.innerHTML += currentQuotes;
		}
	})
	.catch(function(error) {
		console.log(error);
	})
}

function next() {
	page += 1;
	if (page > 1) {
		prevButton.classList.remove("d-none");
	}
}

function previous() {
	if (page > 1) {
		page -= 1;
	}
	if (page === 1) {
		prevButton.classList.add("d-none");
	}
}

///////////// EVENT LISTENERS //////////////

quoteButton.addEventListener("click", function() {
	getQuotes();
	nextButton.classList.remove("d-none");
})

nextButton.addEventListener("click", function(e) {
	console.log(e);
	next();
	getQuotes();
})

prevButton.addEventListener("click", function(e) {
	console.log(e);
	previous();
	getQuotes();
})