
 function addCards() {
    let cardValues = {
        a: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, j: 10, q: 10, k: 10
    };
    
    let cardHeld1 = document.getElementById('card1');
    let cardHeld2 = document.getElementById('card2');
    let suggestion = document.getElementById('suggestion');
    cardHeld1 = cardHeld1.value;
    cardHeld2 = cardHeld2.value;
    let result = cardValues[cardHeld1] + cardValues[cardHeld2];

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