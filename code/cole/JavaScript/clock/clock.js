//clock.js
var timer = document.getElementById('timer');
var laps = document.getElementById('laps');
var toggleBtn = document.getElementById('toggle');
var resetBtn = document.getElementById('reset');
var lapBtn = document.getElementById('lap');
var clearBtn = document.getElementById('clear');

var watch = new Stopwatch(timer, laps);

toggleBtn.addEventListener('click', function() {
  if (watch.isOn) {
    watch.stop();
    this.innerText = 'Start';
  }
  else {
    watch.start();
    this.innerText = 'Stop';
  }
});

resetBtn.addEventListener('click', function(){
  watch.reset();
});

lapBtn.addEventListener('click', function(){
  watch.lap();
});

clearBtn.addEventListener('click', function(){
  laps.innerText = null;
})
function Stopwatch(clockElem, lapElem) {
  var time = 0;
  var interval;
  var offset;

  function update() {
    if (this.isOn) {
      time += delta();
    }
    var formattedTime = timeFormatter(time);
    clockElem.innerText = formattedTime
    console.log(formattedTime);
  }
  function delta() {
    var now = Date.now();
    var timePassed = now - offset;
    offset = now;
    return timePassed;
  }
  function timeFormatter(timeInMilliseconds) {
    var time = new Date(timeInMilliseconds);
    var minutes = time.getMinutes().toString();
    var seconds = time.getSeconds().toString();
    var milliseconds = time.getMilliseconds().toString();

    if (minutes.length < 2) {
      minutes = '0' + minutes;
    }

    if (seconds.length < 2) {
      seconds = '0' + seconds;
    }

    while (milliseconds.length<3) {
      milliseconds = '0' + milliseconds;
    }

    return minutes + ':' + seconds + '.' + milliseconds;
  }

  this.isOn = false;

  this.start = function() {
    if (!this.isOn) {
      interval = setInterval(update.bind(this), 10);
      offset = Date.now();
      this.isOn = true;
    }
  };

  this.stop = function() {
    if (this.isOn) {
      clearInterval(interval);
      interval = null;
      this.isOn = false;
    }
  };

  this.reset = function() {
    time = 0;
    update();
  };
  this.lap = function() {
    newLap = document.createElement('div');
    newLap.innerText = timeFormatter(time);
    lapElem.appendChild(newLap);
  };
}
