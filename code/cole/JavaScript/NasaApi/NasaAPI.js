
new Vue({
  el: '#app',
  data (){
    return {
      data: null,
      chosenDate: null,
      dateData: null,
      dateTempHigh: null,
      dateTempLow: null,
      dateWindAvg: null,
      errorMessage: ''
    }
  },
  methods: {
    showData: function() {
      if (this.chosenDate in this.data.data) {
        this.errorMessage = '';
        this.dateData = this.data.data[this.chosenDate];
        this.dateTempHigh = `${this.dateData.AT.mx}` + '°C';
        this.dateTempLow = `${this.dateData.AT.mn}` + '°C';
        this.dateWindAvg = `${this.dateData.HWS.av}` + ' meters per second';
      }
      else {
        this.errorMessage = 'Please enter a number between 296 and 302';
      }
    }
  },
  mounted () {
    axios
      .get('https://api.nasa.gov/insight_weather/?api_key=Lt3BvyhEO0U5a4eiPDuqi5L2pXsHCn77nDe975fP&feedtype=json&ver=1.0')
      .then(response => (this.data = response))
  }

})
