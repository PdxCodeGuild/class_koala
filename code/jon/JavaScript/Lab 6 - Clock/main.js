



//Clock

// let currentTime = setInterval(function() {

//     let date = new Date();

//     let clockPlacement = document.getElementById('clock');

//     clockPlacement.innerText = `The Current Time is: \n ${date.toLocaleTimeString()}`;

// }, 1000)


//Stopwatch


function stopwatch() {
    //create the stopwatch

    //initialize the timer
    let initTimer = new Date();
    initTimer.setHours(0,0,0,0);
    

    //Get the Hours, Minutes, Seconds
    let hours = initTimer.getHours();
    let minutes = initTimer.getMinutes();
    let seconds = initTimer.getSeconds();
    let milliseconds = initTimer.getMilliseconds();

    //Adds the extra zero in the tens place if the number is less than 10
    hours = (hours < 10 ? "0" : '') + hours;
    minutes = (minutes < 10 ? "0" : '') + minutes;
    seconds = (seconds < 10 ? "0" : '') + seconds;

    //start counting and displaying the new time every second

    startWatch = setInterval(function() {
        //Display the watch
        let stopwatchLocation = document.getElementById('actual-stopwatch');
        let stopwatchDisplay = `${hours}:${minutes}:${seconds}:${milliseconds}`;
        stopwatchLocation.innerText = stopwatchDisplay;
        
    }, 1000)
};

let startButton = document.getElementById('startButton');
let lapButton = document.getElementById('lapButton');

startButton.addEventListener('click', stopwatch);

// let stopwatchDate = new Date();
// stopwatchDate.setHours(0,0,0,0);
// let stopwatchLocation = document.getElementById('actual-stopwatch');

// let minutes = stopwatchDate.getMinutes();
// let seconds = stopwatchDate.getSeconds();
// let ms = stopwatchDate.getMilliseconds();

// stopwatchLocation.innerText = `${minutes}:${seconds}:${ms}`;


