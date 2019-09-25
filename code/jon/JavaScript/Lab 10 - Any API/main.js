let user_input = document.getElementById('user-input');
let submit_button = document.getElementById('submit');
const results = document.getElementById('results'); // where the output is placed



function getResults() {
    axios({
        method: 'post',
        baseURL: 'https://developers.zomato.com/api/v2.1',
        url: 'search',
        params: {
            entity_id:'10640',
            entity_type: 'city',
            count: 5,
            q: user_input.value,
            // establishment_type: 286, //coffee shop
        },
        headers: {
            "user-key": "577576e3fbba11ceadaeed9bc5d1f8b2",
        },
    })
    .then (function(response) {
        let query = response.data.restaurants;
        console.log(query);
        for (let i = 0; i < query.length; i++) {
           
            let result = `
                    <div class='card'>
                        <li>${query[i].restaurant.thumb}</li>
                        <li>Establishment: <a href='`${query[i].url}`}'${query[i].restaurant.name}</li>
                        <li>Address: ${query[i].restaurant.location.address}</li>
                        <li>Phone: ${query[i].restaurant.phone_numbers}</li>
                   </div>
            `
            results.innerHTML += result;
        }
       
    
    })
}

submit_button.addEventListener('click', getResults);