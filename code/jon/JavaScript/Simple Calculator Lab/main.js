let calculations = {
    add: function(a, b) {
        return a + b;
    },
    subtract: function(a, b) {
        return a - b;
    },
    multiply: function(a, b) {
        return a * b;
    },
    divide: function(a, b) {
        return a / b;
    }
}

let operation = prompt('What would you like to do (add, subtract, multiply, divide)? ');

let num1 = parseInt(prompt('What is your first integer? '));

let num2 = parseInt(prompt('What is your second integer? '));


if (operation == 'add') {
    var results = calculations.add(num1, num2);
} else if (operation == 'subtract') {
    
    var results = calculations.subtract(num1, num2);
} else if (operation == 'multiply') {
    
    var results = calculations.multiply(num1, num2);
} else if (operation == 'divide') {
    
    var results = calculations.divide(num1, num2);
}

alert(`Your result is: ${results}`);

