let one = document.getElementById("one");
let two = document.getElementById("two");
let three = document.getElementById("three");
let four = document.getElementById("four");
let five = document.getElementById("five");
let six = document.getElementById("six");
let seven = document.getElementsByClassName("seven");
let eight = document.getElementById("eight");
let nine = document.getElementById("nine");


function math(e) {
  console.log(e);
  let result = document.getElementById("result-field");
  for (let i = 0; i < seven.length; i++) {
    if (e.target == seven[i]) {
      e.stopPropagation();
      result.innerText += "7";
    }
  }
}


let calcButtons = document.getElementsByClassName("button");
console.log(calcButtons);
for (let i = 0; i < calcButtons.length; i++) {
  calcButtons[i].addEventListener("click", math)
}