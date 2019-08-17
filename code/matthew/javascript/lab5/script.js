socials = [
  "facebook.com/mjhughes707",
  "twitter.com/mjhwrites",
  "instagram.com/mjhughes707",
  "linkedin.com/in/mjhughesio",
  "medium.com/@mjhwrites",
  "github.com/mjhughesio"
]

randomSite = function() {
  let randomIndex = Math.random() * socials.length;
  randomIndex = parseInt(randomIndex, 10);
  let link = "https://" + socials[randomIndex];
  window.open(link);
};

randomSite();