let cnv = document.getElementById('cnv');
let ctx = cnv.getContext('2d');

let ball = {
    radius: 20,
    px: Math.floor(Math.random() * cnv.width),
    py: Math.floor(Math.random() * cnv.height),
    vx: Math.floor((2 * Math.random() - 1) * 10),
    vy: Math.floor((2 * Math.random() - 1) * 10)
    // vx: 5,
    // vy: 5
};

console.log(`Ball starts at (${ball.px}, ${ball.py}) and has a vx of ${ball.vx} and a vy of ${ball.vy}`);

//draws the ball 1
ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'black';
ctx.fill();


function main_loop() {

    //Add Gravity to the ball

    const gravity = 0.5;
    ball.vy += gravity;



    // update the ball's position
    ball.px += ball.vx;
    ball.py += ball.vy;


    // check if it hit a boundary and added some Friction
    if (ball.px - ball.radius / 2 < 0 && ball.vx < 0) {
        ball.vx = (-ball.vx * 0.99);
        // ball.vy += gravity;
    }

    if (ball.px + ball.radius / 2 > cnv.width && ball.vx > 0) {
        ball.vx = (-ball.vx * 0.99);
        // ball.vy += gravity;
    }

    if (ball.py - ball.radius / 2 < 0 && ball.vy < 0) {
        ball.vy = (-ball.vy * 0.99);
        // ball.vy += gravity;
    }

    if (ball.py + ball.radius / 2 > cnv.height && ball.vy > 0) {
        ball.vy = (-ball.vy * 0.99);
        // ball.vy += gravity;
    }
    // //Makes so the ball doesn't go below the floor
    // if (ball.py + ball.radius > cnv.height) {
    //     ball.py = cnv.height - ball.radius;
    // }

    console.log(`vy: ${ball.vy}`)
    // draw the ball
    ctx.beginPath();
    // ctx.clearRect(0, 0, cnv.width, cnv.height);
    ctx.fillStyle = "rgba(255,255,255,0.01)";
    ctx.fillRect(0, 0, cnv.width, cnv.height);
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'black';
    ctx.fill();

    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);