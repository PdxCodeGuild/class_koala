let quoteButton = document.getElementById("quote-button");
let target = document.getElementById("target");

quoteButton.addEventListener("click", function(e) {
	axios({
		method: "get",
		baseURL: "https://favqs.com/api/quotes/",
		params: {
			type: "author",
			filter: "Mark+Twain",
		},
		headers: {
			Authorization: 'Token token=""'
		}
	})
	.then(function(response) {
		console.log(response);
		let quotes = response.data.quotes;
		for(let i in quotes) {
			let resultHTML = `
			<div class="mt-4">
				<p>${quotes[i].body}</p>
				<p><a href=${quotes[i].url}>${quotes[i].author}</a></p>
			</div>
			`;
			target.innerHTML += resultHTML;
		}

		// ANOTHER OPTION THAT WORKED, BUT I UNDERSTAND LESS =P
		// let quotes = response.data.quotes;
		// quotes.forEach(obj => {
		// 	let resultHTML = `
		// 	<div class="mt-4">
		// 		<p>${obj.body}</p>
		// 		<p><a href=${obj.url}>${obj.author}</a></p>
		// 	</div>
		// 	`;
		// 	target.innerHTML += resultHTML;
		// });

	})
	.catch(function(error) {
		console.log(error);
	});
});