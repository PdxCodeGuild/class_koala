let card_values = {
    "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "A": 1
}

let counter_values = {
    1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th"
}

alert("Let's play Blackjack!");

let card_list = [];
let again = "y";
let counter = 1;

while (true) {
    let card = prompt(`What's your ${counter_values[counter]} card? `).toUpperCase();
    if (card_values.hasOwnProperty(card) === false) {
        alert("Error... Please enter a valid playing card.");
        continue;
    }

    let card_value = card_values[card];
    card_list.push(card_value);
    const arrSum = arr => arr.reduce((a, b) => a + b, 0);
    let card_total = arrSum(card_list);

    let value_message = (`The value of your hand is currently ${card_total}: `);

    if (card_total < 17) {
        alert(`${value_message}` + " Hit!");
    } else if (card_total < 21) {
        alert(`${value_message}` + " Stay!");
        break;
    } else if (card_total === 21) {
        alert(`${value_message}` + " Blackjack!");
        break;
    } else {
        alert(`${value_message}` + " BUSTED.");
        break
    }

    counter++
}