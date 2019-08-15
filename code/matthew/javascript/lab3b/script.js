let to_meter_table = {
  "feet": .3048, "miles": 1609.34, "meters": 1, "kilometers": 1000, "yards": .9144, "inches": .0254
}

let from_meter_table = {
  "feet": 3.28084, "miles": 0.000621371, "meters": 1, "kilometers": 0.001, "yards": 1.09361, "inches": 39.3701
}

let text_in = document.getElementById("input-distance");
let text_out = document.getElementById("output-distance");
let units_in = document.getElementById("input-units");
let units_out = document.getElementById("output-units");

function conversiona(e) {
  console.log(e);
  let input_distance = parseInt(document.getElementById("input-distance").value);
  let input_units = document.getElementById("input-units").value;
  let output_units = document.getElementById("output-units").value;
  let in_meters = input_distance * to_meter_table[input_units];
  let in_units = in_meters * from_meter_table[output_units];
  if (isNaN(in_units) === true) {
    in_units = 0;
  }
  in_units = Number(Math.round(in_units+'e5')+'e-5');
  text_out.value = in_units;
}

text_in.addEventListener("input", conversiona);
units_in.addEventListener("input", conversiona);

function conversionb(e) {
  console.log(e);
  let input_units = document.getElementById("input-units").value;
  let output_distance = parseInt(document.getElementById("output-distance").value);
  let output_units = document.getElementById("output-units").value;
  let out_meters = output_distance / from_meter_table[output_units];
  let out_units = out_meters / to_meter_table[input_units];
  if (isNaN(out_units) === true) {
    out_units = 0;
  }
  out_units = Number(Math.round(out_units+'e5')+'e-5');
  text_in.value = out_units;
}

text_out.addEventListener("input", conversionb);