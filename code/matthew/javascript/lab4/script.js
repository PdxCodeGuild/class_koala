/***** FUNCTIONS *****/

function create(e) {
  console.log(e);
  let newEvent = document.getElementById("new-text").value;
  let inProgressDiv = document.createElement("div");
  inProgressDiv.className = "in-progress-div";
  let inProgressInput = document.createElement("input");
  inProgressInput.setAttribute("type", "checkbox");
  inProgressInput.className = "checkbox";
  let inProgressPara = document.createElement("p");
  inProgressPara.className = "in-progress-text";
  newEvent = document.createTextNode(newEvent);
  let trashIcon = document.createElement("i");
  trashIcon.className = "fas fa-trash-alt";
  inProgressDiv.appendChild(inProgressInput);
  inProgressDiv.appendChild(inProgressPara);
  inProgressPara.appendChild(newEvent);
  inProgressDiv.appendChild(trashIcon);
  inProgressForm = document.getElementById("in-progress-form");
  inProgressForm.appendChild(inProgressDiv);
  inProgressInput.addEventListener("click", complete);
  trashIcon.addEventListener("click", function(e) {
    console.log(e);
    this.parentNode.remove();
  })
}

function remove(e) {
  console.log(e);
  this.parentNode.remove();
}

function complete(e) {
  console.log(e);
  let checkedText = this.parentNode.innerText;
  this.parentNode.remove();
  let completedDiv = document.createElement("div");
  completedDiv.className = "completed-div";
  let completedPara = document.createElement("p");
  completedPara.className = "completed-text";
  checkedText = document.createTextNode(checkedText);
  completedDiv.appendChild(completedPara);
  completedPara.appendChild(checkedText);
  completedForm = document.getElementById("completed-form");
  completedForm.appendChild(completedDiv);
}

/***** CREATE ITEM *****/

let createBtn = document.getElementById("create-btn");
createBtn.addEventListener("click", create);

/***** DELETE ITEM *****/

let trashCans = document.getElementsByClassName("fa-trash-alt");
for(var i = 0; i < trashCans.length; i++) {
  trashCans[i].addEventListener('click', remove);
}

/***** COMPLETE ITEM *****/

let checkboxes = document.getElementsByClassName("checkbox");
for(var i = 0; i < checkboxes.length; i++) {
  checkboxes[i].addEventListener('click', complete)
}
