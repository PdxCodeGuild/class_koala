let original = document.getElementById("original");
let rotation = document.getElementById("rotation");
let encrypt = document.getElementById("encrypt");
let encrypted = document.getElementById("encrypted");

function rot_cipher(e) {
  console.log(e);
  let cipher_string = "";
  let o_value = original.value;
  let r_value = parseInt(rotation.value);
  let rot_tuple = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
  for (let char of o_value) {
    if (parseInt(rot_tuple.indexOf(char)) < r_value) {
        cipher_string += rot_tuple[parseInt(rot_tuple.indexOf(char)) + r_value];
    } else {
        cipher_string += rot_tuple[parseInt(rot_tuple.indexOf(char)) - r_value];
    }
  }
  encrypted.innerText = cipher_string;
}

encrypt.addEventListener("click", rot_cipher);