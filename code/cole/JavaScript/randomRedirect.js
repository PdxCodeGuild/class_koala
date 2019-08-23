/*randomRedirect.js*/
let message = document.getElementById("message");
let urls = ["http://www.facebook.com", "http://www.youtube.com", "http://www.twitter.com", "http://www.google.com"];
let choice = getRandomIntInclusive(0, 3);
let counter = 5;

setInterval(function(){
  message.innerText = `You will be randomly redirected in ${counter} seconds`;
  counter--;
  if (counter == 0) {
    window.location = urls[choice];
  }
}, 1000);

function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive
}
