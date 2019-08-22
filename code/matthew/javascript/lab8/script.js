let cnv = document.getElementById("cnv");
let ctx = cnv.getContext("2d");

// sets canvas size and background
let width = 1400;
let height = 760;
ctx.fillStyle = "rgba(255, 255, 255, 0.25)";
ctx.fillRect(0, 0, width, height);


// sets ball size, location and velocity
let ball = {
  radius: 100,
  px: Math.random()*width, // ball's x location
  py: Math.random()*height, // ball's y location
  vx: (2*Math.random()-1)*10, // ball's x velocity
  vy: (2*Math.random()-1)*10 // ball's y velocity
};

ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = "#f9f9f9";
ctx.fill();

function drawBallLines() {
  // draws bottom line of pentagon (left to right)
  ctx.beginPath();
  ctx.moveTo(ball.px - 20, ball.py + 25);
  ctx.lineTo(ball.px + 20, ball.py + 25);
  ctx.lineWidth = 2.5;
  ctx.stokeStyle = "black";
  ctx.stroke();
  
  // draws right line of pentagon (mid-right to bottom right)
  ctx.beginPath();
  ctx.moveTo(ball.px + 30, ball.py - 12.5);
  ctx.lineTo(ball.px + 20, ball.py + 25);
  ctx.lineWidth = 2.5;
  ctx.stokeStyle = "black";
  ctx.stroke();
  
  // draws left line of pentagon (mid-left to bottom left)
  ctx.beginPath();
  ctx.moveTo(ball.px - 30, ball.py - 12.5);
  ctx.lineTo(ball.px - 20, ball.py + 25);
  ctx.lineWidth = 2.5;
  ctx.stokeStyle = "black";
  ctx.stroke();

  // draws top right line of pentagon (mid-right to top middle)
  ctx.beginPath();
  ctx.moveTo(ball.px + 30, ball.py - 12.5);
  ctx.lineTo(ball.px, ball.py - 31.25);
  ctx.lineWidth = 2.5;
  ctx.stokeStyle = "black";
  ctx.stroke();

  // draws top left line of pentagon (mid-left to top middle)
  ctx.beginPath();
  ctx.moveTo(ball.px - 30, ball.py - 12.5);
  ctx.lineTo(ball.px, ball.py - 31.25);
  ctx.lineWidth = 2.5;
  ctx.stokeStyle = "black";
  ctx.stroke();
}

drawBallLines();