///////////// VUE //////////////

new Vue({
	el: '#app',
	data () {
		return {
			restaurants: null,
			searchValue: null,
		}
	},
	methods: {
		listCarts: function() {
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
					"q": this.searchValue,
					"establishment_type": 81,
					"count": 20,
				}
			})
			.then((response) => {
				console.log(response.data.restaurants);
				this.restaurants = response.data.restaurants;
			})
			.catch(function(error) {
				console.log(error);
			})
		}
	},
	mounted() {
		this.listCarts()
	}
})