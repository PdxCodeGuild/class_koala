
let enter = document.getElementsByName("button");
let body = document.querySelector("body");
amountEntered = false;
enter[0].onclick = function() {
  let enter = document.getElementsByName("button");
  if(amountEntered == false){
    let numAmount = document.getElementById("numAmount");
    var a = document.createElement("div");
    a.innerText = "Enter the numbers you would like to average.";
    body.appendChild(a);
    i = 0;
    while(i < numAmount.value){
      var a = document.createElement("div");
      body.appendChild(a);
      var x = document.createElement("input");
      x.setAttribute("type", "text");
      x.setAttribute("name", "value");
      a.appendChild(x);
      i++
    }
    var a = document.createElement("div");
    body.appendChild(a);
    let btn = document.createElement("button");
    btn.addEventListener("click", calculateAverage)
    btn.setAttribute("id", "button2");
    btn.innerText = "Enter";
    a.appendChild(btn);
  }
 enter2 = document.getElementById("button2");
 amountEntered = true;
}

function calculateAverage() {
  nums = document.getElementsByName("value");
  let total = 0;
  i = 0;
  while (i < nums.length) {
    total = parseInt(total) + parseInt(nums[i].value);
    i++;
  }
  average = parseInt(total)/nums.length
  a = document.createElement("div");
  a.innerText = `The average is ${average}`;
  body.appendChild(a);
}
