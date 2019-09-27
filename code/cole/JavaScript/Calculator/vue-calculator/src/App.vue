<template>
  <div id="app">
    <div class="display">{{ current || '0'}}</div>
    <div @click="clear" class="operator-btn">C</div>
    <div @click="sign" class="operator-btn">+/-</div>
    <div @click="percent" class="operator-btn">%</div>
    <div @click="divide" class="operator-btn">÷</div>
    <div @click="append(7)" class="btn">7</div>
    <div @click="append(8)" class="btn">8</div>
    <div @click="append(9)" class="btn">9</div>
    <div @click="multiply" class="operator-btn">x</div>
    <div @click="append(4)" class="btn">4</div>
    <div @click="append(5)" class="btn">5</div>
    <div @click="append(6)" class="btn">6</div>
    <div @click="subtract" class="operator-btn">-</div>
    <div @click="append(1)" class="btn">1</div>
    <div @click="append(2)" class="btn">2</div>
    <div @click="append(3)" class="btn">3</div>
    <div @click="add" class="operator-btn">+</div>
    <div @click="add_zero" id="zero" class="btn">0</div>
    <div @click="dot" class="btn">.</div>
    <div @click="equal" class="operator-btn">=</div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      current: '',
      operator: '',
      operatorClicked: false,
      previous: '',
    }
  },
  methods: {
    clear() {
      this.current = '';
    },
    sign() {
      this.current = this.current.charAt(0) === '-' ?
        this.current.slice(1) : `-${this.current}`;
    },
    percent() {
      this.current = `${parseFloat(this.current) / 100}`
    },
    append(number) {
      if (this.operatorClicked) {
        this.clear();
        this.operatorClicked = false;
      }
      this.current = `${this.current}${number}`
    },
    add_zero() {
      if (this.current !== '') {
        this.append(0)
      }
    },
    dot() {
      if (this.current.indexOf('.') === -1) {
        this.append('.');
      }
    },
    setPrevious() {
      this.previous = this.current;
      this.operatorClicked = true;
    },
    divide() {
      this.operator = (a, b) => a / b;
      this.setPrevious();
    },
    multiply() {
      this.operator = (a, b) => a * b;
      this.setPrevious();
    },
    subtract() {
      this.operator = (a, b) => a - b;
      this.setPrevious();
    },
    add() {
      this.operator = (a, b) => a + b;
      this.setPrevious();
    },
    equal() {
      this.current = `${this.operator(parseFloat(this.previous),parseFloat(this.current))}`;
      this.previous = ''
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgb(245,245,245);
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(50px, auto);
  font-size: 40px;
  width: 400px;
  margin: 0 auto;

}

#zero {
  grid-column: 1/3;
  padding-right: 100px;
}

.display {
  grid-column: 1/5;
  background-color: teal;
  border: 1px solid rgb(20,20,20);
  text-align: right;
  padding-right: 37px;
  padding-right: 37px;
}

.btn{
  background-color: rgb(60,60,60);
  border: 1px solid rgb(20,20,20);
}

.operator-btn{
  background-color: rgb(116, 180, 232);
  border: 1px solid rgb(20,20,20);
}
</style>
