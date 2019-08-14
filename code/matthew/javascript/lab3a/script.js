let to_meter_table = {
    "feet": .3048, "miles": 1609.34, "meters": 1, "kilometers": 1000, "yards": .9144, "inches": .0254
}

let from_meter_table = {
    "feet": 3.28084, "miles": 0.000621371, "meters": 1, "kilometers": 0.001, "yards": 1.09361, "inches": 39.3701
}

let distance = parseInt(prompt("What is the distance? "));
let input_unit = prompt("What are the input units? ").toLowerCase();

if (input_unit.startsWith("f")) {
    input_unit = "feet";
} else if (input_unit.startsWith("mi")) {
    input_unit = "miles";
} else if (input_unit.startsWith("me")) {
    input_init = "meters";
} else if (input_unit.startsWith("k")) {
    input_unit = "kilometers";
} else if (input_unit.startsWith("y")) {
    input_unit = "yards";
} else if (input_unit.startsWith("i")) {
    input_unit = "inches";
} else {
    alert("Error. Requires a unit of measurement (e.g. miles, meters, feet, etc.) Exiting... ");
}

let in_meters = distance * to_meter_table[input_unit];

let output_unit = prompt("What are the output units? ").toLowerCase();

if (output_unit.startsWith("f")) {
    output_unit = "feet";
} else if (output_unit.startsWith("mi")) {
    output_unit = "miles";
} else if (output_unit.startsWith("me")) {
    output_unit = "meters";
} else if (output_unit.startsWith("k")) {
    output_unit = "kilometers";
} else if (output_unit.startsWith("y")) {
    output_unit = "yards";
} else if (output_unit.startsWith("i")) {
    output_unit = "inches";
} else {
    alert("Error. Requires a unit of measurement (e.g. miles, meters, feet, etc.) Exiting... ");
}

let in_units = in_meters * from_meter_table[output_unit];

alert(`${distance} ${input_unit} converts to ${in_units} ${output_unit}.` )





