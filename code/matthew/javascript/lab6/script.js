setInterval (function() {
  let d = new Date();
  let h = d.getHours();
  let m = d.getMinutes();
  let s = d.getSeconds();
  m = ( m < 10 ? "0" : "" ) + m;
  s = ( s < 10 ? "0" : "" ) + s;
  let t = h + ":" + m + ":" + s;
  document.getElementById("clock-time").innerText = t;
}, 1000);