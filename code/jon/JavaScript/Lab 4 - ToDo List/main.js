/*

let thingToDo = document.getElementById('thingToDo');
let postButton = document.getElementById('postButton');
let todoList = document.getElementById('todoList');
let todoListCompleted = document.getElementById('todoListCompleted');

*/

let list = [];

function post() {
    let thingToDo = document.getElementById('thingToDo').value;
    let todoList = document.getElementById('todoList');
    let item = document.createElement('li');

    item.innerText = thingToDo;

    todoList.appendChild(item);

    todoList.push(thingToDo);

    

    
    // list.push(thingToDo);
    
    // todoList.insertAdjacentHTML("beforeend", `${list}<br>`);

}

let postButton = document.getElementById('postButton');
postButton.addEventListener('click', post);