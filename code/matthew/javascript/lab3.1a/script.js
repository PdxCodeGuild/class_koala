// PALINDROME CHECKER

function check_palindrome(s) {
    s = s.replace(/\s+/g, '');
    let reversedString = s.split("").reverse().join("");
    if (s === reversedString) {
        alert(`${word} is a palindrome.`);
    } else {
        alert(`${word} is not a palindrome.`);
    }
}

let word = prompt("Enter a word: ").toLowerCase();
check_palindrome(word);

// ANAGRAM CHECKER

function check_anagram(word1, word2) {
    let original1 = word1;
    word1 = word1.toLowerCase().replace(" ", "").split("").sort().join("");
    let original2 = word2;
    word2 = word2.toLowerCase().replace(" ", "").split("").sort().join("");
    if (word1 === word2) {
        alert(`${original1} and ${original2} are anagrams.`);
    } else {
        alert(`${original1} and ${original2} are not anagrams.`);
    }
}

word1 = prompt("Enter the first word:");
word2 = prompt("Enter the second word:");
check_anagram(word1, word2);