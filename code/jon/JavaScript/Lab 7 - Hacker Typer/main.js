let randomText = ["adfa", "http:", "\n", "fun", "EToH", "click", "Reaper", "R34P3R", "SabEr", "hACk", "\n", "WWW", "random", "crazy", "wArneR", "HacK", "plANet", "thE", "raNdoM", "cereal","\n", "PytHOn", "csS", "jaVasCrypt", "\n", "coFFEe", "//", ",", "!!!", "#245", "dafdlj9", "993ddbacr_", "brEakER", "   ", "%#", "#@%^##&*", "\n"];

let screenPlacement = document.getElementById('canvas');

document.body.addEventListener('keydown', function() {
    if (!event.shiftKey) {
        let randomNumber = Math.floor(Math.random() * randomText.length);
        let randomWord = randomText[randomNumber];
        screenPlacement.innerText += randomWord;
    } else if (event.shiftKey) {
        alert('Command Accepted!');
        document.body.innerText = '';
    }

})

console.log(randomText)