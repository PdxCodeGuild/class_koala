let originalWord = document.getElementById('originalWord');
let button = document.getElementById('button');
let cipherAnswer = document.getElementById('cipher');


function cipher() {
    let word = originalWord.value;
    let letters = 'abcdefghijklmnopqrstuvwxyz';
    let cipherLetters = 'nopqrstuvwxyzabcdefghijklm';
    let encrypted = '';

    for (let i = 0; i < word.length; i++) {
        letterIndex = letters.indexOf(word[i]);
        encrypted += cipherLetters.substr(letterIndex, 1);
    };
    
    cipherAnswer.innerText = encrypted;
}

button.addEventListener('click', cipher);


