let canvas = document.getElementById("canvas");
let width = canvas.width;
let height = canvas.height;

let ball = {
    radius: 4,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};

console.log(ball.vx);
console.log(ball.vy);

let ctx = canvas.getContext("2d");

function main_loop() {
  ball.vy += .01;
  ball.px += ball.vx;
  ball.py += ball.vy;
  if (ball.px > width || ball.px < 0) {
    ball.vx = -ball.vx;
    ball.vx = ball.vx*.9;
  }
  if (ball.py > height || ball.py < 0) {
    ball.vy = -ball.vy;
    ball.vy = ball.vy*.9;
  }
  ctx.clearRect(0,0,width,height);
  ctx.beginPath();
  ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
  ctx.fillStyle = 'green';
  ctx.fill();
  window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);
