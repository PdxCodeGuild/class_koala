new Vue({
    el: '#vue',
    data() {
        return{
            previous: null,
            current: '',
            operator: null,
            operatorClicked: false,
        }
    },
    methods: {
        clear() {
            this.current = '';
        },
        sign() {
            this.current = this.current.charAt(0) === '-' ? this.current.slice(1) : `-${this.current}`;
        },
        percent() {
            this.current = `${parseFloat(this.current) / 100}`;
        },
        append(number) {
            if (this.operatorClicked) {
                this.current = '';
                this.operatorClicked = false;
            }
            this.current = `${this.current}${number}`;
            
        },
        dot() {
            if(this.current.indexOf('.') === -1) {
                this.append('.');
            }
        },
        divide() {
            this.operator = (a,b) => a/b;
            this.previous = this.current;
            this.operatorClicked = true;
        },
        multiply() {
            this.operator =  (a,b) => a*b;
            this.previous = this.current;
            this.operatorClicked = true;
        },
        subtract() {
            this.operator = (a,b) => a-b; 
                this.previous = this.current;
                this.operatorClicked = true;
        },
        add() {
            this.operator = (a,b) => a+b; 
                this.previous = this.current;
                this.operatorClicked = true;
        },
        equals() {
            this.current = `${this.operator(
            parseFloat(this.current), 
            parseFloat(this.previous)
            )}`;
            this.previous = null;
        }, 
    },
})
    
