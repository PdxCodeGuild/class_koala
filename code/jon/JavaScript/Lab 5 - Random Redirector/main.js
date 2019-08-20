function randomSites () {
let random_urls = [
    'https://www.google.com',
    'https://www.twitter.com',
    'https://www.linkedin.com',
    'https://www.pdxcodeguild.com'
];

let min = 0;
let max = random_urls.length;
randomNumber = Math.floor(Math.random() * (max - min + 1));

 location = random_urls[randomNumber];
};
//Version 2 JS

//Display Countdown Timer

let timer = setTimeout(myTimer, 5000)

function myTimer () {
    let seconds = document.getElementById('countdown').textContent;
    let countdown = setInterval(function() {
        seconds--;
        if (seconds <=0) clearInterval(countdown) {
            randomSites();
        }
    })

};

//After 5 seconds, redirects to a random URL listed above

