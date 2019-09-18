///////////// ROOT VUE //////////////

new Vue({
	el: "#app",
	data () {
		return {
			searchValue: null,
			typeValue: null,
			quoteResults: [],
		}
	},
	methods: {
		getQuotes: function() {
			axios({
				method: "get",
				baseURL: "https://favqs.com/api/quotes/",
				params: {
					page: 1,
					filter: this.searchValue,
					type: this.typeValue,
				},
				headers: {
					Authorization: 'Token token=""'
				}
			})
			.then((response) => {
				this.quoteResults = response.data.quotes;
				console.log(this.quoteResults);
			})
			.catch(function(error) {
				console.log(error);
			})
		}
	},
	mounted() {
		this.getQuotes();
	}
})

document.addEventListener('DOMContentLoaded', function() {
	var elems = document.querySelectorAll('select');
	var instances = M.FormSelect.init(elems);
});




///////////// GLOBAL VARIABLES //////////////

// let page = 1;

// let quoteButton = document.getElementById("quote-button");
// let target = document.getElementById("target");
// let prevButton = document.getElementById("prevButton");
// let nextButton = document.getElementById("nextButton");
// let userInput = document.getElementById("user-input");

///////////// FUNCTIONS //////////////


// function next() {
// 	page += 1;
// 	if (page > 1) {
// 		prevButton.classList.remove("d-none");
// 	}
// }

// function previous() {
// 	if (page > 1) {
// 		page -= 1;
// 	}
// 	if (page === 1) {
// 		prevButton.classList.add("d-none");
// 	}
// }

// function keyPress(e) {
// 	if (e.which === 13) {
// 	  getQuotes();
// 	  nextButton.classList.remove("d-none");
// 	  e.preventDefault();
// 	}
//   }