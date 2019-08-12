let cardValues = {
    a: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    j: 10,
    q: 10,
    k: 10,
};

function addCards(card1, card2, card3) {
    let first = cardValues[card1];
    let second = cardValues[card2];
    let third = cardValues[card3];

    return total = first + second + third;
}

firstCard = prompt('What is your first card? ');
secondCard = prompt('What is your second card? ');
thirdCard = prompt('What is your third card? ');

result = addCards(firstCard, secondCard, thirdCard);

if (result < 17) {
    alert(`Total is ${result}.  You should hit!`)
} else if(result >= 17 && result < 21) {
    alert(`Total is ${result}.  You should stay!`)
} else if (result === 21) {
    alert(`Total is ${result}.  Blackjack!`)
} else {
    alert(`Total is ${result}.  Already Busted!`)
};