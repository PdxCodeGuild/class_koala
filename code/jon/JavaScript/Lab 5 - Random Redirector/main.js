let random_urls = [
    'https://www.google.com',
    'https://www.twitter.com',
    'https://www.linkedin.com',
    'https://www.pdxcodeguild.com'
];

let min = 0;
let max = random_urls.length;
randomNumber = Math.floor(Math.random() * (max - min + 1));

 location = random_urls[randomNumber];