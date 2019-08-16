/***** CREATE ITEM *****/

let create_btn = document.getElementById("create-btn");

function create(e) {
  console.log(e);
  let new_event = document.getElementById("new-text").value;
  document.getElementsByClassName("in-progress-text")[0].innerText = new_event;
}

create_btn.addEventListener("click", create);


/***** DELETE ITEM *****/

let trashCans = document.getElementsByClassName("fa-trash-alt");

for(var i = 0; i < trashCans.length; i++) {
  trashCans[i].addEventListener('click', function(e) {
    console.log(e);
    this.parentNode.remove();
  });
}

/***** COMPLETE ITEM *****/

let checkboxes = document.getElementsByClassName("checkbox");

for(var i = 0; i < checkboxes.length; i++) {
  checkboxes[i].addEventListener('click', function(e) {
    console.log(e);
    let checkedText = this.parentNode.innerText;
    console.log(checkedText);
    console.log(typeof checkedText);
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
  });
}
