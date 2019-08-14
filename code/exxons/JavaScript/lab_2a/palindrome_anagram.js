

let user_word = prompt("which word would you like to check?");







function check_anagram () {
    lower_case = `${user_word2}`.toLowerCase();
    
    no_space_string = lower_case.replace(/\s/g,'');

    
    non_arranged_word = no_space_string;

    no_space_string = non_arranged_word.split('').sort().join('');

    arranged_word = no_space_string;
    
    
    console.log(no_space_string);

    if (lower_case === user_word2) {
        alert(`${lower_case} and ${user_word2} are anagrams!`);
    } else {
        alert(`${lower_case} and ${user_word2} are not anagrams!`);
    }


}





function check_palindrome() {

const str = user_word

lower = str.toLowerCase();

const userPalword = lower 
    .split('')
    .reverse()
    .join('');
    
    console.log(userPalword);
    

    if (user_word === userPalword){
        alert(`The word is a palindrome`);
    } else {    alert('Sorry, thats not a palindrome.');
};


}








check_palindrome(); 


let user_word2 = prompt("now enter another word to see if it is an anagram for your word:");


check_anagram()