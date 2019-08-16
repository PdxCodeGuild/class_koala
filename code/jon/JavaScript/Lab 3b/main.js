function is_palindrome() {
    let palindromeWord = document.getElementById('is_palindrome').value;
    palindromeWord = palindromeWord.toLowerCase();

    let palindromeNoSpace = palindromeWord.replace(/\s+/g, '');

    let palindromeReversed = palindromeNoSpace.split('').reverse().join('');

    let palindromeAnswer = document.getElementById('palindrome_answer');

    if (palindromeNoSpace === palindromeReversed) {
        palindromeAnswer.innerText = `${palindromeWord} is a Palindrome!`;
    } else {
        palindromeAnswer.innerText = `${palindromeWord} is not a Palindrome!`;
    };
};

function is_anagram() {
    let word1 = document.getElementById('anagram1').value;
    
    let word2 = document.getElementById('anagram2').value;

    let anagramAnswer = document.getElementById('anagram_answer');

    let word1NoSpaces = word1.replace(/\s+/g, '');

    let word2NoSpaces = word2.replace(/\s+/g, '');

    let word1Sorted = word1NoSpaces.split('').sort().join('');

    let word2Sorted = word2NoSpaces.split('').sort().join('');

    if (word1Sorted === word2Sorted) {
        anagramAnswer.innerText = `${word1} and ${word2} are both Anagrams`;
    } else {
        anagramAnswer.innerText = `${word1} and ${word2} are not Anagrams`;
    }
}

let palindromeButton = document.getElementById('check_pali_answer');

palindromeButton.addEventListener('click', is_palindrome);

let anagramButton = document.getElementById('check_anagram_answer');

anagramButton.addEventListener('click', is_anagram);

