socials = [
  "facebook.com/mjhughes707",
  "twitter.com/mjhwrites",
  "instagram.com/mjhughes707",
  "linkedin.com/in/mjhughesio",
  "medium.com/@mjhwrites",
  "github.com/mjhughesio"
]

function randomSite() {
  let randomIndex = Math.random() * socials.length;
  randomIndex = parseInt(randomIndex, 10);
  let link = "https://" + socials[randomIndex];
  window.open(link);
};

window.onload = function() {
  let counter = 5;
  setInterval(function() {
    counter--;
    if (counter >= 0) {
      countdown = document.getElementById("countdown");
      countdown.innerText = counter;
    }
    if (counter === 0) {
      randomSite();
    }
  }, 1000)
};