class ATM {
    constructor(balance = 0, transactions = []) {
        this.balance = balance;
        this.transactions = transactions;
    };

    checkBalance() {
        return (`Your balance is ${this.balance}.`);
        // alert(`Your balance is $${balance}.`)
    };

    deposit(amount) {
        balance += amount;
        this.transactions.push(`User deposited ${amount}.`);
    };

    checkWithdrawal(amount) {
        result = balance - amount;
        if (result >= 0){
            return true;
        } else {
            return false;
        }
    };

    withdraw(amount) {
        if (checkWithdrawal == true) {
            balance -= amount;
            this.transactions.push(`User withdrew ${amount}.`);
            alert(`User withdrew ${amount}`);
        } else {
            alert(`Sorry! You don\'t have enough to cover that withdrawal.`);
        }
    };

    printTransactions() {
        result = transactions;
        alert(result);
    };
};

choice = prompt(`What would you like to do today? Balance, Deposit, Withdraw, Transactions, Exit`);

choice = choice.toLowerCase();

let session = new ATM(choice);

if (choice === 'exit') {
    alert('Thanks for using the ATM!');
    
} else if(choice ==='balance') {
    alert(session.checkBalance());
} else if(choice ==='deposit') {
    amount = prompt('How much would you like to deposit? ');
    session.deposit(amount);
} else if(choice ==='withdraw') {
    amount = prompt('How much would you like to withdraw? ');
    session.withdraw(amount);
} else if(choice ==='transactions') {
    session.printTransactions();
}


