function cipher(string) {
    let letters = 'abcdefghijklmnopqrstuvwxyz';
    let cipher = 'nopqrstuvwxyzabcdefghijklm';
    let encrypted = '';

    for (let i = 0; i < string.length; i++) {
        letterIndex = letters.indexOf(string[i]);
        encrypted = encrypted + cipher.substr(letterIndex,1);
    };
    return encrypted;
}

word = prompt('What word would you like to encrypt? ').toLowerCase();

cipher(word);
encryptedWord = cipher(word);
alert(`Original word: ${word} \nEncrypted word: ${encryptedWord}`);