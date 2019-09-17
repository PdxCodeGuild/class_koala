///////////// VUE //////////////

new Vue({
	el: '#app',
	data () {
		return {
			restaurants: null
		}
	},
	methods: {
	},
	mounted: function() {
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
				// "q": searchValue,
				"establishment_type": 81,
				"count": 5,
			}
		})
		.then((response) => {
			console.log(response);
			console.log(response.data.restaurants[0].restaurant.thumb)
			this.restaurants = response.data.restaurants;
		})
		.catch(function(error) {
			console.log(error);
		})
	}
})