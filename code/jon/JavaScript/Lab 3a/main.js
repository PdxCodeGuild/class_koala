// class ATM {
//     constructor(balance = 0, transactions = []) {
//         this.balance = balance;
//         this.transactions = transactions;
//     };

//     checkBalance() {
//         alert(`Your balance is ${this.balance}.`);
//         // alert(`Your balance is $${balance}.`)
//     };

//     deposit(amount) {
//         balance += amount;
//         this.transactions.push(`User deposited ${amount}.`);
//     };

//     checkWithdrawal(amount) {
//         result = balance - amount;
//         if (result >= 0){
//             return true;
//         } else {
//             return false;
//         }
//     };

//     withdraw(amount) {
//         if (checkWithdrawal == true) {
//             balance -= amount;
//             this.transactions.push(`User withdrew ${amount}.`);
//             alert(`User withdrew ${amount}`);
//         } else {
//             alert(`Sorry! You don\'t have enough to cover that withdrawal.`);
//         }
//     };

//     printTransactions() {
//         result = transactions;
//         alert(result);
//     };
// };

// choice = prompt(`What would you like to do today? Balance, Deposit, Withdraw, Transactions, Exit`);

// choice = choice.toLowerCase();

// let session = new ATM(choice);

// if (choice === 'exit') {
//     alert('Thanks for using the ATM!');
    
// } else if(choice ==='balance') {
//     (session.checkBalance());
// } else if(choice ==='deposit') {
//     amount = prompt('How much would you like to deposit? ');
//     session.deposit(amount);
// } else if(choice ==='withdraw') {
//     amount = prompt('How much would you like to withdraw? ');
//     session.withdraw(amount);
// } else if(choice ==='transactions') {
//     session.printTransactions();
// }

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
