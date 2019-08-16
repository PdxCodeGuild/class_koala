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
  trashCans[i].addEventListener('click', function() {
    document.getElementsByClassName("in-progress-div")[0].remove();
  });
}