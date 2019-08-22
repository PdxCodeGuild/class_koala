
var cnv = document.getElementById('my_canvas');
var ctx = cnv.getContext('2d');
var balls;


var ball = {
    radius: 15,
    px: Math.random()*1000,
    py: Math.random()*500,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,


draw: function() {
ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'green';
ctx.fill();
}

};

function bounce(){
    ctx.clearRect(0,0, cnv.width, cnv.height);
    window.requestAnimationFrame(bounce);
    ball.draw();
    ball.px += ball.vx;
    ball.py += ball.vy;
    if (ball.py + ball.vy > cnv.height || ball.py + ball.vy < 0) {
        ball.vy = -ball.vy;
      }
      if (ball.px + ball.vx > cnv.width || ball.px + ball.vx < 0) {
        ball.vx = -ball.vx;
      }
}

window.requestAnimationFrame(bounce);


ball.draw();
