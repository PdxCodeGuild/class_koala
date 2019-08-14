function rot_cipher(input_string, rotation_amount) {
    let rot_tuple = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
    let cipher_string = "";

    for (let char of input_string) {
        if (parseInt(rot_tuple.indexOf(char)) < rotation_amount) {
            cipher_string += rot_tuple[parseInt(rot_tuple.indexOf(char)) + rotation_amount];
        } else {
            cipher_string += rot_tuple[parseInt(rot_tuple.indexOf(char)) - rotation_amount];
        }
    };
    return cipher_string;

}

let input_string = prompt("Please enter a word to be encrypted: ").toLowerCase();

let rotation_amount = parseInt(prompt("Please enter the amount of rotation to be used: "));

cipher_string = rot_cipher(input_string, rotation_amount);

alert(`The encrypted message is '${cipher_string}'.`);