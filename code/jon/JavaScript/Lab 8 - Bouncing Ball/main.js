
let cnv = document.getElementById('cnv');
let ctx = cnv.getContext('2d');

let ball = {
    radius: 10,
    px: Math.random() * cnv.width,
    py: Math.random()* cnv.height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};

//draws the ball
ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'black';
ctx.fill();

function main_loop() {
    
    // update the ball's position
    ball.px += ball.vx;
    ball.py += ball.vy;

    // check if it hit a boundary
    if(ball.px - ball.radius /2 < 0 && ball.vx < 0) {
        ball.vx = -ball.vx;
    }
    
    if (ball.px + ball.radius /2 > cnv.width && ball.vx > 0) {
        ball.vx = -ball.vx;
    }

    if(ball.py - ball.radius /2 < 0 && ball.vy < 0) {
        ball.vy = -ball.vy;
    }
    
    if (ball.py + ball.radius /2 > cnv.width && ball.vy > 0) {
        ball.vy = -ball.vy;
    }
    // draw the ball
    ctx.clearRect(ball.px, ball.py, cnv.width, cnv.height);
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'black';
    ctx.fill();

    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);