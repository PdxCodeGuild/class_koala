////////// VUE COMPONENTS //////////

Vue.component('clearbutton', {
  template: `<div class="btn" @click="$emit('clear')">C</div>`,
});

Vue.component('signbutton', {
  template: `<div class="btn" @click="$emit('sign')">±</div>`,
});

Vue.component('percentbutton', {
  template: `<div class="btn" @click="$emit('percent')">%</div>`,
});

Vue.component('numbutton', {
  props: ['num'],
  template: `<div class="btn" @click="$emit('append', num)">{{ num }}</div>`,
});

Vue.component('divbutton', {
  template: `<div class="btn operator" @click="$emit('divide')">÷</div>`,
});

Vue.component('multbutton', {
  template: `<div class="btn operator" @click="$emit('multiply')">×</div>`,
});

Vue.component('subbutton', {
  template: `<div class="btn operator" @click="$emit('subtract')">−</div>`,
});

Vue.component('addbutton', {
  template: `<div class="btn operator" @click="$emit('add')">+</div>`,
});

Vue.component('dotbutton', {
  template: `<div class="btn" @click="$emit('dot')">.</div>`,
});

Vue.component('equalbutton', {
  template: `<div class="btn operator" @click="$emit('equal')">=</div>`,
});


////////// VUE ROOT //////////

new Vue({
  el: "#app",
  data() {
    return {
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
      this.current = this.current.charAt(0) === '-' ? 
        this.current.slice(1) : `-${this.current}`;
    },
    percent() {
      this.current = `${parseFloat(this.current) / 100}`;
    },
    dot() {
      if (this.current.indexOf('.') === -1) {
        this.append('.');
      }
    },
    append(number, $event) {
      if (this.operatorClicked) {
        this.current = '';
        this.operatorClicked = false;
      }
      this.current = `${this.current}${number}`;
    },
    setPrevious() {
      this.previous = this.current;
      this.operatorClicked = true;
    },
    divide() {
      this.operator = (a, b) => b / a;
      this.setPrevious();
    },
    multiply() {
      this.operator = (a, b) => a * b;
      this.setPrevious();
    },
    subtract() {
      this.operator = (a, b) => b - a;
      this.setPrevious();
    },
    add() {
      this.operator = (a, b) => a + b;
      this.setPrevious();
    },
    equal() {
      this.current = `${this.operator(
        parseFloat(this.current), 
        parseFloat(this.previous)
      )}`;
      this.previous = null;
    }
  }
})