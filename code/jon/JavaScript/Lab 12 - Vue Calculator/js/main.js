new Vue({
    el: '#vue',
    data() {
        return{
            current: '',
            operator: null,
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
            this.current = `${this.current}${number}`;
        },
        dot() {
            if(this.current.indexOf('.') === -1) {
                this.append('.');
            }
        },
        divide() {
            // this.current = 
        },
        multiply() {

        },
        subtract() {

        },
        add() {

        },
        equals() {

        }, 


    },
})
    
