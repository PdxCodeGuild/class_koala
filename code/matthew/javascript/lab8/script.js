function drawBall() {
  // DRAWS BALL CIRCLE AND FILLS IT WHITE-ISH //
  ctx.beginPath();
  ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
  ctx.fillStyle = "#f9f9f9";
  ctx.fill();

  // DRAWS OUTER SHADOW //
  ctx.beginPath();
  ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
  ctx.strokeStyle = "rgba(0, 0, 0, .5)";
  ctx.lineWidth = 2;
  ctx.stroke();

  // DRAWS INNER PENTAGON //
  // bottom line; from left to right
  ctx.beginPath();
  ctx.moveTo(ball.px - 20, ball.py + 25);
  ctx.lineTo(ball.px + 20, ball.py + 25);
  ctx.strokeStyle = "black";
  ctx.stroke();
  
  // right line; from mid-right to bottom right
  ctx.beginPath();
  ctx.moveTo(ball.px + 30, ball.py - 12.5);
  ctx.lineTo(ball.px + 20, ball.py + 25);
  ctx.stroke();
  
  // left line; from mid-left to bottom left
  ctx.beginPath();
  ctx.moveTo(ball.px - 30, ball.py - 12.5);
  ctx.lineTo(ball.px - 20, ball.py + 25);
  ctx.stroke();

  // top right line; from mid-right to top middle
  ctx.beginPath();
  ctx.moveTo(ball.px + 30, ball.py - 12.5);
  ctx.lineTo(ball.px, ball.py - 31.25);
  ctx.stroke();

  // top left line; from mid-left to top middle
  ctx.beginPath();
  ctx.moveTo(ball.px - 30, ball.py - 12.5);
  ctx.lineTo(ball.px, ball.py - 31.25);
  ctx.stroke();

  // DRAWS LINES FROM EACH CORNER OF PENTAGON // 
  // top line
  ctx.beginPath();
  ctx.moveTo(ball.px, ball.py - 31.25);
  ctx.lineTo(ball.px, ball.py - 75);
  ctx.stroke();

  // mid-left line
  ctx.beginPath();
  ctx.moveTo(ball.px - 30, ball.py - 12.5);
  ctx.lineTo(ball.px - 71, ball.py - 31);
  ctx.stroke();

  // bottom-left line
  ctx.beginPath();
  ctx.moveTo(ball.px - 20, ball.py + 25);
  ctx.lineTo(ball.px - 50, ball.py + 60);
  ctx.stroke();

  // bottom-right line
  ctx.beginPath();
  ctx.moveTo(ball.px + 20, ball.py + 25);
  ctx.lineTo(ball.px + 50, ball.py + 60);
  ctx.stroke();

  // mid-right line
  ctx.beginPath();
  ctx.moveTo(ball.px + 30, ball.py - 12.5);
  ctx.lineTo(ball.px + 71, ball.py - 31);
  ctx.stroke();

  // DRAWS OUTER PENTAGONS //
  // top two lines
  ctx.beginPath();
  ctx.moveTo(ball.px, ball.py - 75);
  ctx.lineTo(ball.px - 35, ball.py - 93);
  ctx.stroke(); // left
  ctx.moveTo(ball.px, ball.py - 75);
  ctx.lineTo(ball.px + 35, ball.py - 93);
  ctx.stroke(); // right

  // mid-left two lines
  ctx.beginPath();
  ctx.moveTo(ball.px - 71, ball.py - 31);
  ctx.lineTo(ball.px - 78, ball.py - 62);
  ctx.stroke(); // top
  ctx.moveTo(ball.px - 71, ball.py - 31);
  ctx.lineTo(ball.px - 99, ball.py - 4);
  ctx.stroke(); // bottom

  // mid-right two lines
  ctx.beginPath();
  ctx.moveTo(ball.px + 71, ball.py - 31);
  ctx.lineTo(ball.px + 78, ball.py - 62);
  ctx.stroke(); // top
  ctx.moveTo(ball.px + 71, ball.py - 31);
  ctx.lineTo(ball.px + 99, ball.py - 4);
  ctx.stroke(); // bottom

  // bottom-left two lines
  ctx.beginPath();
  ctx.moveTo(ball.px - 50, ball.py + 60);
  ctx.lineTo(ball.px - 88, ball.py + 46);
  ctx.stroke(); // left
  ctx.moveTo(ball.px - 50, ball.py + 60);
  ctx.lineTo(ball.px - 42, ball.py + 90);
  ctx.stroke(); // right

  // bottom-right two lines
  ctx.beginPath();
  ctx.moveTo(ball.px + 50, ball.py + 60);
  ctx.lineTo(ball.px + 88, ball.py + 46);
  ctx.stroke(); // left
  ctx.moveTo(ball.px + 50, ball.py + 60);
  ctx.lineTo(ball.px + 42, ball.py + 90);
  ctx.stroke(); // right
}

// NEGATES VELOCITY AND INCREASES FRICTION //
function flipAndFricX() { // left and right borders
  ball.vx *= -1;
  ball.vx *= friction;
  ball.vy *= friction;
}
function flipAndFricY () { // top and bottom borders
  ball.vy *= -1;
  ball.vx *= friction;
  ball.vy *= friction;
}

function moveBall() {
  ball.px += ball.vx; // horizontal speed based on velocity
  ball.py += ball.vy; // vertical speed based on velocity
  // left border
  if (ball.px - ball.radius < 0) {
    ball.px = ball.radius + movement;
    flipAndFricX();
  // right border
  } else if (ball.px + ball.radius > width) {
      ball.px = width - ball.radius - movement;
      flipAndFricX();
  }
  // top border
  if (ball.py - ball.radius < 0) {
    ball.py = ball.radius + movement;
    flipAndFricY();
  // bottom border
  } else if (ball.py + ball.radius > height) {
      ball.py = height - ball.radius - movement;
      flipAndFricY();
  }
}

function loop() {
  ctx.clearRect(0, 0, width, height); // eliminates "image drag"
  moveBall();
  drawBall();
  window.requestAnimationFrame(loop);
}

// sets initial variables
let cnv = document.getElementById("cnv");
let ctx = cnv.getContext("2d");

// sets canvas size
let width = 1400;
let height = 760;

// sets ball size, location and velocity
let ball = {
  radius: 100,
  px: Math.random() * width, // ball's x location
  py: Math.random() * height, // ball's y location
  vx: 12, // ball's x velocity
  vy: 12 // ball's y velocity
};

// sets loop variables
let friction = .99; // slows down ball after each collision with image border
let movement = .001; // moves x or y positions

window.requestAnimationFrame(loop); // enters loop