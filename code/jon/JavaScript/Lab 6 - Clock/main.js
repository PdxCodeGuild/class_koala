
//Clock

let currentTime = setInterval(function() {

    let date = new Date();

    let clockPlacement = document.getElementById('clock');

    clockPlacement.innerText = `The Current Time is: \n ${date.toLocaleTimeString()}`;

}, 1000)


//Stopwatch

let startWatch;
function stopwatch() {
    //create the stopwatch

    //initialize the timer
    let initTimer = new Date();
    initTimer.setHours(0,0,0,0);

    let timer = `00:00:00`;
    let mainTimer = document.getElementById('actual-stopwatch');

    mainTimer.innerText = `${timer}`;
    
    //start counting and displaying the new time every second

    startWatch = setInterval(function() {
        //Get the Hours, Minutes, Seconds
        let hours = initTimer.getHours();
        let minutes = initTimer.getMinutes();
        let seconds = initTimer.getSeconds();
        //Adds the extra zero in the tens place if the number is less than 10
        hours = (hours < 10 ? "0" : '') + hours;
        minutes = (minutes < 10 ? "0" : '') + minutes;
        seconds = (seconds < 10 ? "0" : '') + seconds;

        //Display the watch
        let stopwatchLocation = document.getElementById('actual-stopwatch');

        initTimer.setSeconds(initTimer.getSeconds() + 1);

        let stopwatchDisplay = `${hours}:${minutes}:${seconds}`;
        stopwatchLocation.innerText = stopwatchDisplay;
        
        
    }, 1000)
};

let lapTimerList;
function lap() {
    //Get current value of what is in the stopwatch currently
    let stopwatchValue = document.getElementById('actual-stopwatch').innerText

    //target the Lap window
    lapTimerList = document.getElementById('lap');

    //Create the text to be displayed in the lap timer list
    let newLi = document.createElement('li');

    // let timeToAdd = document.createTextNode(stopwatchValue);
    
    let timeToAdd = document.createTextNode(`Lap: ${stopwatchValue}`);
    newLi.appendChild(timeToAdd);

    lapTimerList.appendChild(newLi);
}

function stop() {
    clearInterval(startWatch);
}

function reset() {
    let stopwatchLocation = document.getElementById('actual-stopwatch');
    clearInterval(startWatch);
    stopwatchLocation.innerText = `00:00:00`;
    let lapList = document.getElementById('lap');
    // lapTimerList.parentNode.removeChild(lapList);
    while (lapList.firstChild) {
        lapList.removeChild(lapList.firstChild);
    }
}


let startButton = document.getElementById('startButton');
let lapButton = document.getElementById('lapButton');
let stopButton = document.getElementById('stopButton');
let ResetButton = document.getElementById('resetButton');

startButton.addEventListener('click', stopwatch);
lapButton.addEventListener('click', lap);
stopButton.addEventListener('click', stop);
ResetButton.addEventListener('click', reset);

// let stopwatchDate = new Date();
// stopwatchDate.setHours(0,0,0,0);
// let stopwatchLocation = document.getElementById('actual-stopwatch');

// let minutes = stopwatchDate.getMinutes();
// let seconds = stopwatchDate.getSeconds();
// let ms = stopwatchDate.getMilliseconds();

// stopwatchLocation.innerText = `${minutes}:${seconds}:${ms}`;


