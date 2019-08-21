let nonDisplay = ["C", "±", "%", "÷", "×", "−", "+", "="];

function math(e) {
  console.log(e);
  let result = document.getElementById("result-field");
  if (result.innerText == "0") {
    result.innerText = "";
  }
  if (nonDisplay.includes(this.children[0].innerText) == true) {
    e.preventDefault();
  } else {
    result.innerText += this.children[0].innerText;
  }
}

let calcButtons = document.getElementsByClassName("button");
console.log(calcButtons);
for (let i = 0; i < calcButtons.length; i++) {
  calcButtons[i].addEventListener("click", math)
}