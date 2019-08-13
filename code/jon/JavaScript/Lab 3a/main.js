
// Palindrome Program

// function checkPalindrome(word) {
//     let word2 = word.replace(/\s+/g, '');
//     let reversed = word2.split('').reverse().join('');
//     console.log(`reversed: ${reversed}`);
//     console.log(`word2 is ${word2}`);
//     if (word2 == reversed){
//         alert(`The word is a palendrome`);
//     } else {
//         alert('Sorry, thats not a palindrome.');
        
//     };
// };

// let word = prompt('Enter a word: ');

// checkPalindrome(word)

//Anagram program

function checkAnagram(word1, word2) {

    //Removes the spaces in the string
    let word1_noSpaces = word1.replace(/\s+/g, '');
    let word2_noSpaces = word2.replace(/\s+/g, '');

    //Sorts the letters in the string in alphabetical order
    let word1_sorted = word1_noSpaces.split('').sort().join('');
    let word2_sorted = word2_noSpaces.split('').sort().join('');

    //Checks to see if the 2 words are anagrams

    if (word1_sorted === word2_sorted) {
        alert(`${word1} and ${word2} are anagrams!`);
    } else {
        alert(`${word1} and ${word2} are not anagrams!`);
    }
};



let word1 = prompt('Enter the first word: ');
word1 = word1.toLowerCase();
let word2 = prompt('Enter the second word: ');
word2 = word2.toLowerCase();

checkAnagram(word1, word2);
