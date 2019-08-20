// CLOCK //

setInterval (function() {
  let d = new Date();
  let h = d.getHours();
  let m = d.getMinutes();
  let s = d.getSeconds();
  h = (h < 10 ? "0" : "") + h;
  m = (m < 10 ? "0" : "") + m;
  s = (s < 10 ? "0" : "") + s;
  let t = h + ":" + m + ":" + s;
  document.getElementById("clock-time").innerText = t;
}, 1000);

// STOPWATCH - START //

let stopTimer; // related to STOP function
function stopwatch() {
  document.getElementById("stopwatch-time").innerText = "00:00:00";
  let d = new Date();
  d.setHours(0, 0, 0, 0);
  stopTimer = setInterval (function() {
    d.setSeconds(d.getSeconds() + 1);
    let h = d.getHours();
    let m = d.getMinutes();
    let s = d.getSeconds();
    h = (h < 10 ? "0" : "") + h;
    m = (m < 10 ? "0" : "") + m;
    s = (s < 10 ? "0" : "") + s;
    let t = h + ":" + m + ":" + s;
    document.getElementById("stopwatch-time").innerText = t;
  }, 1000);
}

var start = document.getElementById("start");
start.addEventListener("click", stopwatch);

// STOPWATCH - STOP //

var stop = document.getElementById("stop");
stop.addEventListener("click", function() {
  clearInterval(stopTimer)
});

// STOPWATCH - LAP //

function lapCount() {
  let lapTime = document.getElementById("stopwatch-time").innerText;
  let newLapTime = document.createElement("p");
  newLapTime.innerText = lapTime;
  let laps = document.getElementById("stopwatch-laps");
  laps.appendChild(newLapTime);
}

var lap = document.getElementById("lap");
lap.addEventListener("click", lapCount);

// STOPWATCH - RESET //

var reset = document.getElementById("reset");
reset.addEventListener("click", function() {
  clearInterval(stopTimer);
  document.getElementById("stopwatch-time").innerText = "00:00:00";
});

// STOPWATCH - DEFAULT //

document.getElementById("stopwatch-time").innerText = "00:00:00"; // sets default on load

// COUNTDOWN

function countdown() {
  // stores all of the user values
  let cd = document.getElementById("countdown-date").value;
  let ch = document.getElementById("countdown-hours").value;
  let cm = document.getElementById("countdown-minutes").value;
  let cs = document.getElementById("countdown-seconds").value;
  let countdownDate = new Date(`${cd} ${ch}:${cm}:${cs}`).getTime(); // compiles together
  let counter = setInterval(function() {
    let now = new Date().getTime();
    let distance = countdownDate - now;
    // math to determine days, etc. based on seconds
    let days = Math.floor(distance / (1000 * 60 * 60 * 24));
    let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);
    document.getElementById("countdown-time").innerText = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    // sets what occurs when countdown reaches zero
    if (distance <= 1) {
      clearInterval(counter);
      document.getElementById("countdown-time").innerText = "0d 0h 0m 0s";
      document.getElementById("countdown-complete").style.backgroundImage = "url('balloons.jpg')";
    }
  }, 1000);
}

let countdownStart = document.getElementById("countdown-start");
countdownStart.addEventListener("click", countdown);