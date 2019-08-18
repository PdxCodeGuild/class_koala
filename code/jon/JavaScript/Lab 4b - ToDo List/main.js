 const addButton = document.getElementById('submitButton');
 const list = document.getElementById('list');
 const completedArea = document.getElementById('completedArea');
 
 
 /* Create the HTML code to add an item */

 function addItem() {
   let item = document.getElementById('todo').value;
   const list = document.getElementById('list');
   //creating new <li> and <i> for FontAwesome icons
   const newItem = document.createElement('li');
   newItem.className = 'notDone'
   const newFontAwesome = document.createElement('i');
   newFontAwesome.className = 'far fa-check-circle';
   const newTrash = document.createElement('i');
   newTrash.className = 'fas fa-times-circle';
   newItem.appendChild(newFontAwesome);
   newEvent = document.createTextNode(item);
   newItem.appendChild(newEvent);
   newItem.appendChild(newTrash);
   list.appendChild(newItem);

   newTrash.addEventListener('click', remove);
 }

 function remove() {
    this.parentNode.remove();
 }
 
 const newAddItemButton = document.getElementById('submitButton');

 newAddItemButton.addEventListener('click', addItem);
 

 


