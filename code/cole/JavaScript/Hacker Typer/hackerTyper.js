
let fakeCode = `i = float(input("Please enter a distance."))
inUnit = input("What is the input unit?")
outUnit = input("What is the desired output unit?")


if inUnit == outUnit:
    print(f"{i} {inUnit}")
elif inUnit == "m" or inUnit == "meters":
    if outUnit == "mi" or outUnit == "miles":
        i = i/1609.34
        print(f"{i} mi")
    elif outUnit == "ft" or outUnit == "feet":
        i = i/0.3048
        print(f"{i} ft")
    elif outUnit == "km" or outUnit == "kilometers":
        i = i/1000
        print(f"{i} km")
    elif outUnit == "yd" or outUnit == "yards":
        i = i/0.9144
        print(f"{i} yd")
    elif outUnit == "in" or outUnit -- "inches":
        i = i/0.0254
        print(f"{i} in")

elif inUnit == "ft" or inUnit == "feet":
    if outUnit == "m" or outUnit == "meters":
        i = i*0.3048
        print(f"{i} m")
    elif outUnit == "mi" or outUnit == "miles":
        i = i/5280
        print(f"{i} mi")
    elif outUnit == "km" or outUnit == "kilometers":
        i = i/3280.84
        print(f"{i} km")
    elif outUnit == "yd" or outUnit == "yards":
        i = i/3
        print(f"{i} yd")
    elif outUnit == "in" or outUnit -- "inches":
        i = i*12
        print(f"{i} in")

elif inUnit == "mi" or inUnit == "miles":
    if outUnit == "m" or outUnit == "meters":
        i = i*1609.34
        print(f"{i} mi")
    elif outUnit == "ft" or outUnit == "feet":
        i = i*5280
        print(f"{i} ft")
    elif outUnit == "km" or outUnit == "kilometers":
        i = i*1.60934
        print(f"{i} km")
    elif outUnit == "yd" or outUnit == "yards":
        i = i*1760
        print(f"{i} yd")
    elif outUnit == "in" or outUnit -- "inches":
        i = i*63360
        print(f"{i} in")

elif inUnit == "km" or inUnit == "kilometers":
    if outUnit == "mi" or outUnit == "miles":
        i = i/1.60934
        print(f"{i} mi")
    elif outUnit == "ft" or outUnit == "feet":
        i = i*3280.84
        print(f"{i} ft")
    elif outUnit == "m" or outUnit == "meters":
        i = i*1000
        print(f"{i} m")
    elif outUnit == "yd" or outUnit == "yards":
        i = i*1093.613
        print(f"{i} yd")
    elif outUnit == "in" or outUnit -- "inches":
        i = i*39370.08
        print(f"{i} in")

elif inUnit == "yd" or inUnit == "yards":
    if outUnit == "mi" or outUnit == "miles":
        i = i/1760
        print(f"{i} mi")
    elif outUnit == "ft" or outUnit == "feet":
        i = i*3
        print(f"{i} ft")
    elif outUnit == "km" or outUnit == "kilometers":
        i = i/1093.613
        print(f"{i} km")
    elif outUnit == "m" or outUnit == "meters":
        i = i*0.9144
        print(f"{i} m")
    elif outUnit == "in" or outUnit -- "inches":
        i = i*36
        print(f"{i} in")

elif inUnit == "in" or inUnit == "inches":
    if outUnit == "mi" or outUnit == "miles":
        i = i/63360
        print(f"{i} mi")
    elif outUnit == "ft" or outUnit == "feet":
        i = i/12
        print(f"{i} ft")
    elif outUnit == "km" or outUnit == "kilometers":
        i = i/39370.08
        print(f"{i} km")
    elif outUnit == "yd" or outUnit == "yards":
        i = i/36
        print(f"{i} yd")
    elif outUnit == "m" or outUnit -- "meters":
        i = i*0.0254
        print(f"{i} m")
`
let body = document.getElementById("body");
let page = document.getElementById("html")
let allLines = fakeCode.split(/\r\n|\n/);
i = 0;

function addText() {
  body.innerText += `${allLines[i]}\n`;
  i++;
}

page.addEventListener('keydown', addText);
