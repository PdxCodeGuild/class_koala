/*toDo.js*/
let enter = document.getElementById("addItem");
let clear = document.getElementById("clear");
let main = document.getElementById("mainDiv");
let complete = document.getElementById("completed")

enter.onclick = function addItem() {
  userInput = document.getElementById("item");
  let newLine = document.createElement("div");
  newLine.innerText = userInput.value;
  newLine.addEventListener("click", completed);
  main.appendChild(newLine);
}

function completed() {
  this.remove();
  complete.appendChild(this);
  this.addEventListener("click", remove);
}

function remove() {
  this.remove();
}
