let create_btn = document.getElementById("create-btn");

function create(e) {
  console.log(e);
  let new_event = document.getElementById("new-text").value;
  document.getElementsByClassName("in-progress-text")[0].innerText = new_event;
}

create_btn.addEventListener("click", create);