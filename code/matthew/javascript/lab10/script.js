///////////// GLOBAL VARIABLES //////////////

let searchField = document.getElementById("search-field");
let searchButton = document.getElementById("search-button");
let target = document.getElementById("target");

///////////// FUNCTIONS //////////////

function listCarts() {
	let searchValue = document.getElementById("search-field").value;
	axios({
		method: "get",
    baseURL: "https://developers.zomato.com/api/v2.1/",
    url: "search",
		headers: {
      "user-key": "",
    },
    params: {
      "entity_id": 286,
      "entity_type": "city",
      "q": searchValue,
      "establishment_type": 81,
      "count": 5,
    }
	})
	.then(function(response) {
		console.log(response);
		let restaurants = response.data.restaurants;
		target.innerHTML = "";
		for(let r of restaurants) {			
			let results = `
      <div class="mt-4">
        <p><img src="${r.restaurant.thumb}" /></p>
        <h2>${r.restaurant.name}</h2>
        <p>${r.restaurant.location.address}</p>
        <p>${r.restaurant.location.locality}</p>
        <p>${r.restaurant.cuisines}</p>
        <hr />
			</div>
			`;
			target.innerHTML += results;
		}
	})
	.catch(function(error) {
		console.log(error);
	})
}

function keyPress(e) {
	if (e.which === 13) {
	  listCarts();
	  e.preventDefault();
	}
  }

///////////// EVENT LISTENERS //////////////

searchField.addEventListener("keydown", keyPress, function(e) {
	console.log(e);
});

searchButton.addEventListener("click", function() {
	listCarts();
})