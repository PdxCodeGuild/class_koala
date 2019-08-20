function randomSites() {
    let random_urls = [
        'http://www.google.com',
        'http://www.yahoo.com',
        'http://www.sjsharks.com',
        'http://www.pdxcodeguild.com'
    ];

    let min = 0;
    let max = random_urls.length;
    randomNumber = Math.floor(Math.random() * (max - min + 1));

    location = random_urls[randomNumber];
};
//Version 2 JS

//Display Countdown Timer
let timeLeft = 5;
let countdown = setInterval(function () {
    document.getElementById('countdown-timer').innerText = `${timeLeft} second(s) until a random page appears!`;
    timeLeft -= 1;
    if (timeLeft == 0) {
        clearInterval(countdown);
        randomSites();
    }
}, 1000);