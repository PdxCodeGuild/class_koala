// CLOCK //

setInterval (function() {
  let d = new Date();
  let h = d.getHours();
  let m = d.getMinutes();
  let s = d.getSeconds();
  m = (m < 10 ? "0" : "") + m;
  s = (s < 10 ? "0" : "") + s;
  let t = h + ":" + m + ":" + s;
  document.getElementById("clock-time").innerText = t;
}, 1000);

// STOPWATCH - START //

function stopwatch() {
  let d = new Date();
  d.setHours(0, 0, 0, 0);
  setInterval (function() {
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