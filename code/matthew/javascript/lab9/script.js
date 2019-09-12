///////////// GLOBAL VARIABLES //////////////

let page = 1;

let quoteButton = document.getElementById("quote-button");
let target = document.getElementById("target");
let prevButton = document.getElementById("prevButton");
let nextButton = document.getElementById("nextButton");
let userInput = document.getElementById("user-input");

///////////// FUNCTIONS //////////////

function getQuotes() {
	let userFilter = document.getElementById("user-input").value;
	axios({
		method: "get",
		baseURL: "https://favqs.com/api/quotes/",
		params: {
			page: page,
			filter: userFilter,
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

function keyPress(e) {
	if (e.which === 13) {
	  getQuotes();
	  nextButton.classList.remove("d-none");
	  e.preventDefault();
	}
  }

///////////// EVENT LISTENERS //////////////

quoteButton.addEventListener("click", function() {
	getQuotes();
	nextButton.classList.remove("d-none");
})

userInput.addEventListener("keydown", keyPress, function(e) {
	console.log(e);
});

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