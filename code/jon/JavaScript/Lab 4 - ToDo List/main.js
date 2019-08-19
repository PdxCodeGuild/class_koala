//Creating List

function list() {
    //grabbing to do list
    const todoList = document.getElementById('list');

    //grabbing the value of the input
    let input = document.getElementById('todo').value;

    //Create an <li> </li>
    const newListItem = document.createElement('li');

    //Create an unchecked icon
    let uncheckedIcon = document.createElement('i');
    uncheckedIcon.className = 'far fa-check-circle';
    

    //Create a Delete icon
    let deleteIcon = document.createElement('i');
    deleteIcon.className = 'fas fa-times-circle';
    

    //Creates <li><i class='far fa-check-circle'></li>
    newListItem.appendChild(uncheckedIcon);

    //Creates <li><i class='far fa-check-circle'> input </li>
    newEvent = document.createTextNode(input);
    newListItem.appendChild(newEvent);

    //Creates <li><i class='far fa-check-circle'></i> input <i>'fas fa-times-circle'</i></li>
    newListItem.appendChild(deleteIcon);

    //Places everything into #list
    todoList.appendChild(newListItem);

    //Delete item from #list when the deleteIcon is clicked

    deleteIcon.addEventListener('click', function () {
        this.parentNode.remove();
    });

    //Move item from list to the "completed" area

    uncheckedIcon.addEventListener('click', completed);
};

function completed() {
    //Grabs the completed area <ul>
    let completedArea = document.getElementById('completedArea');

    //Gets and stores the text in the list item associated with the #completedIcon
    let completedText = this.parentNode.innerText;

    //Deletes the list item from the list
    this.parentNode.remove();

    //Creates new <li> </li>
    let newCompletedItem = document.createElement('li');

    //Create a Completed icon
    let completedIcon = document.createElement('i');
    completedIcon.className = 'fas fa-check-circle';
    completedIcon.id = 'completed';
    
    newCompletedItem.appendChild(completedIcon);

    //Creates <li>
    newCompletedText = document.createTextNode(completedText);
    newCompletedItem.appendChild(newCompletedText);

    completedArea.appendChild(newCompletedItem);
};


//Actions

//Listen for the "add button" click to add a new list item
let submitButton = document.getElementById('submitButton');
submitButton.addEventListener('click', list)