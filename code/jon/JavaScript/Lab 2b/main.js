//Need to add functionality to assign the Ace to 11 if the total was less than 21

 function addCards() {
    let cardValues = {
        a: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, j: 10, q: 10, k: 10, n: 0
    };
    
    let cardHeld1 = document.getElementById('card1');
    let cardHeld2 = document.getElementById('card2');
    let cardHeld3 = document.getElementById('card3');
    let cardHeld4 = document.getElementById('card4');
    let cardHeld5 = document.getElementById('card5');
    let cardHeld6 = document.getElementById('card6');
    let suggestion = document.getElementById('suggestion');
     cardHeld1 = cardHeld1.value;
     cardHeld2 = cardHeld2.value;
     cardHeld3 = cardHeld3.value;
     cardHeld4 = cardHeld4.value;
     cardHeld5 = cardHeld5.value;
     cardHeld6 = cardHeld6.value;

    let result = cardValues[cardHeld1] + cardValues[cardHeld2] + cardValues[cardHeld3] + cardValues[cardHeld4] + cardValues[cardHeld5] + cardValues[cardHeld6];

    if (result < 17) {
        suggestion.innerText = `Total is ${result}.  You should HIT!`;
    } else if ( result >= 17 && result < 21) {
        suggestion.innerText = `Total is ${result}.  You should STAY!`;
    } else if (result === 21) {
        suggestion.innerText = `Total is ${result}.  BLACKJACK!`;
    } else {
        suggestion.innerText = `Total is ${result}.  You\'ve already BUSTED!`;
    }
 };

 let submitButton = document.getElementById('button');
 submitButton.addEventListener('click', addCards);

 let reset = document.getElementById('reset');
 reset.addEventListener('click', function() {
     document.getElementById('myForm').reset();
     document.getElementById('suggestion').innerText = '';
 });