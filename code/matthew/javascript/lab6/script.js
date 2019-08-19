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




// STOPWATCH - RESET //

var reset = document.getElementById("reset");
reset.addEventListener("click", function() {
  clearInterval(stopTimer);
  document.getElementById("stopwatch-time").innerText = "00:00:00";
});