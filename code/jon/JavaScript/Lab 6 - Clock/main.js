



let currentTime = setInterval(function() {

    let date = new Date();

    let clockPlacement = document.getElementById('clock');

    clockPlacement.innerText = `The Current Time is: \n ${date.toLocaleTimeString()}`;

}, 1000)

