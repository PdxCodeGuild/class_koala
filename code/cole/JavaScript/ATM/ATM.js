/*ATM.js*/
let depositStart = document.getElementById("Deposit");
let withdrawStart = document.getElementById("Withdraw");
let balanceCheck = document.getElementById("Balance");
let historyCheck = document.getElementById("History");
let depositDiv = document.getElementById("depositDiv");
let withdrawDiv = document.getElementById("withdrawDiv");
let balanceDiv = document.getElementById("balanceDiv");
let historyDiv = document.getElementById("historyDiv");

let balance = 0;
let log = [];
let depositClicked = false;
let withdrawClicked = false;
let balanceClicked = false;
let historyClicked = false;

depositStart.onclick = function(){
  if (depositClicked == false) {
    depositBox = document.createElement("div");
    depositBox.innerText = "Enter Deposit Amount: ";
    depositDiv.appendChild(depositBox)
    depositInput = document.createElement("input");
    depositButton = document.createElement("button");
    depositButton.innerText = "Enter";
    depositButton.addEventListener("click", deposit)
    depositBox.appendChild(depositInput);
    depositBox.appendChild(depositButton);
    depositClicked = true;
  }
  else {
    depositDiv.removeChild(depositBox);
    depositClicked = false;
  }
}

withdrawStart.onclick = function(){
  if (withdrawClicked == false) {
    withdrawBox = document.createElement("div");
    withdrawBox.innerText = "Enter Withdrawal Amount: ";
    withdrawDiv.appendChild(withdrawBox)
    withdrawInput = document.createElement("input");
    withdrawButton = document.createElement("button");
    withdrawButton.innerText = "Enter";
    withdrawButton.addEventListener("click", withdraw)
    withdrawBox.appendChild(withdrawInput);
    withdrawBox.appendChild(withdrawButton);
    withdrawClicked = true;
  }
  else {
    withdrawDiv.removeChild(withdrawBox);
    withdrawClicked = false;
  }
}

balanceCheck.onclick = function(){
  if (balanceClicked == false) {
    balanceBox = document.createElement("div");
    balanceBox.innerText = `Your current balance is $${balance}`;
    balanceDiv.appendChild(balanceBox);
    balanceClicked = true;
  }
  else {
    balanceDiv.removeChild(balanceBox);
    balanceClicked = false;
  }
}

historyCheck.onclick = function(){
  if (historyClicked == false) {
    let i = 0;
    historyBox = document.createElement("div");
    historyDiv.appendChild(historyBox)
    while (i < log.length){
      historyLine = document.createElement("div");
      historyLine.innerText = log[i];
      historyBox.appendChild(historyLine);
      i++;
    }
    historyClicked = true;
  }
  else {
    historyDiv.removeChild(historyBox);
    historyClicked = false;
  }
}

function deposit(){
  balance = parseFloat(balance) + parseFloat(depositInput.value);
  log.push(`User Deposited $${depositInput.value}`);
  depositDiv.removeChild(depositBox);
  depositClicked = false;
}

function withdraw(){
  balance = parseFloat(balance) - parseFloat(withdrawInput.value);
  log.push(`User Withdrew $${withdrawInput.value}`)
  withdrawDiv.removeChild(withdrawBox);
  withdrawClicked = false;
}
