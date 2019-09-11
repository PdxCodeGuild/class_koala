let quoteButton = document.getElementById("quote-button");
let target = document.getElementById("target");

quoteButton.addEventListener("click", function(e) {
	axios({
		method: "get",
		url: "https://favqs.com/api/qotd",
		// headers: {
		// 	Authorization: "Token token = ''"
		// }
	})
	.then(function(response) {
		console.log(response);
		let resultHTML = `
			<p class="mt-4">${response.data.quote.body}</p>
			<p><a href=${response.data.quote.url}>${response.data.quote.author}</a></p>
		`;
		target.innerHTML = resultHTML;
	})
	.catch(function(error) {
		console.log(error);
	});
});