///////////// VUE COMPONENTS //////////////

Vue.component('prev-button', {
	props: [],
	template:
		`<li id="prevbutton" class="disabled" @click="pagePrev">
			<a href="#!">
			<i class="material-icons">chevron_left</i>
			</a>
			</i>
		</li>`,
	methods: {
		pagePrev: function () {
			if (this.$parent.currentPage === 2) {
				prevbutton.classList.add("disabled");
				};
			if (this.$parent.currentPage === 1) {
				prevbutton.classList.remove("waves-effect");
				};
			if (this.$parent.currentPage > 1) {
				this.$parent.currentPage--;
				this.$parent.getQuotes();
				};
			},
	}
})

Vue.component('next-button', {
	props: [],
	template:
		`<li id="nextbutton" class="waves-effect" @click="pageNext">
			<a href="#!">
			<i class="material-icons">chevron_right</i>
			</a>
			</i>
		</li>`,
	methods: {
			pageNext: function() {
				this.$parent.currentPage++;
				this.$parent.getQuotes();
				prevbutton.classList.remove("disabled");
				prevbutton.classList.add("waves-effect")
			},
	}
})



///////////// ROOT VUE //////////////

new Vue({
	el: "#app",
	data () {
		return {
			searchValue: null,
			typeValue: null,
			quoteResults: [],
			currentPage: 1,
			perPage: 5,
			pages: [],
		}
	},
	methods: {
		getQuotes: function() {
			axios({
				method: "get",
				baseURL: "https://favqs.com/api/quotes/",
				params: {
					page: this.currentPage,
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
		},
	},
	mounted() {
		this.getQuotes();
	}
})



///////////// MATERIALIZE //////////////

document.addEventListener('DOMContentLoaded', function() {
	var elems = document.querySelectorAll('select');
	var instances = M.FormSelect.init(elems);
});