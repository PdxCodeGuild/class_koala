//pick6.js
let winNumsDiv = document.getElementById("winningNums");
let yourNumsDiv = document.getElementById("yourNums");
let balanceDiv = document.getElementById("balance");
let buy = document.getElementById("button");
let buy100 = document.getElementById("button2")
let buy100000 = document.getElementById("button3")
let balance = 0;
let yourNums = [];
let winningNums = [];
winningNums = pick6(winningNums);
let winNumValues = document.createElement("div");
winNumValues.innerText = winningNums;
winNumsDiv.appendChild(winNumValues);
let fillerDiv = document.createElement("div");
yourNumsDiv.appendChild(fillerDiv);

buy.onclick = function(){
  balance -= 2;
  yourNums = pick6(yourNums);
  let yourNumValues = document.createElement("div");
  yourNumValues.innerText = yourNums;
  yourNumsDiv.replaceChild(yourNumValues, yourNumsDiv.lastChild);
  balance += compareNums(winningNums, yourNums)
  balanceDiv.innerText = `Balance: $${balance}`;
}

buy100.onclick = function(){
  let i = 0;
  while (i < 100){
    balance -= 2;
    yourNums = pick6(yourNums);
    let yourNumValues = document.createElement("div");
    yourNumValues.innerText = yourNums;
    yourNumsDiv.replaceChild(yourNumValues, yourNumsDiv.lastChild);
    balance += compareNums(winningNums, yourNums)
    balanceDiv.innerText = `Balance: $${balance}`;
    i++
  }
}

buy100000.onclick = function(){
  let i = 0;
  while (i < 100000){
    balance -= 2;
    yourNums = pick6(yourNums);
    let yourNumValues = document.createElement("div");
    yourNumValues.innerText = yourNums;
    yourNumsDiv.replaceChild(yourNumValues, yourNumsDiv.lastChild);
    balance += compareNums(winningNums, yourNums)
    balanceDiv.innerText = `Balance: $${balance}`;
    i++
  }
}

function pick6(list) {
  let i = 0;
  while (i < 6) {
    let x = getRandomIntInclusive(1, 99);
    list[i] = ` ${x}`;
    i++;
  }
  return list;
}

function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive
}

function compareNums(list1, list2) {
  let i = 0;
  let matches = 0;
  while (i < 6) {
    if (list1[i] == list2[i]) {
      matches++
    }
    i++
  }
  if (matches == 0) {
    return 0;
  }
  if (matches == 1) {
    console.log("1 match")
    return 4;
  }
  if (matches == 2) {
    console.log("2 matches")
    return 7;
  }
  if (matches == 3) {
    console.log("3 matches")
    return 100;
  }
  if (matches == 4) {
    console.log("4 matches")
    return 50000;
  }
  if (matches == 5) {
    console.log("5 matches")
    return 1000000;
  }
  if (matches == 6) {
    console.log("6 matches")
    return 25000000;
  }
}
