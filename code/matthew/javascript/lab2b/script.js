let card1 = document.getElementById("card1");
let card2 = document.getElementById("card2");
let card3 = document.getElementById("card3");
let card4 = document.getElementById("card4");
let card5 = document.getElementById("card5");
let evaluate = document.getElementById("evaluate");
let advice = document.getElementById("advice");

function bj_advice() {
  let card_list = [];
  let card_value = card1.value;
  card_list.push(card_value);
  card_value = card2.value;
  card_list.push(card_value);
  card_value = card_values[(card3.value).toUpperCase()];
  if (card_value === undefined) {
    card_value = 0;
  }
  card_list.push(card_value);
  card_value = card_values[(card4.value).toUpperCase()];
  if (card_value === undefined) {
    card_value = 0;
  }
  card_list.push(card_value);
  card_value = card_values[(card5.value).toUpperCase()];
  if (card_value === undefined) {
    card_value = 0;
  }
  card_list.push(card_value);
  const arrSum = arr => arr.reduce((a, b) => a + b, 0);
  let card_total = arrSum(card_list);
  if (card_total < 17) {
    advice.value = `${card_total} - Hit!`;
  } else if (card_total < 21) {
    advice.value = `${card_total} - Stay!`;
  } else if (card_total === 21) {
    advice.value = `${card_total} - Blackjack!`;
  } else if (card_total > 21)  {
    advice.value = `${card_total} - BUSTED.`;
  }
}

evaluate.addEventListener("click", bj_advice);