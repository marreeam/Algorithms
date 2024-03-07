function rotateString() {
    var string = "Zebra-493";
    var lenString = string.length;
    var rotationFactor = Math.floor(Math.random() * 10) + 1;
    var characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var charactersLowercased = "abcdefghijklmnopqrstuvwxyz";
    var digits = "0123456789";
    var newString = [];

    for (var i = 0; i < lenString; i++) {
        if (string[i].toUpperCase() === string[i]) { // Check if the character is uppercase
            var index = characters.indexOf(string[i]);
            var newIndex = index + rotationFactor;
            if (newIndex >= 26) {
                newIndex -= 26; // Wrap around if index goes beyond 'Z'
            }
            newString.push(characters.charAt(newIndex));
        } else if (!isNaN(parseInt(string[i]))) { // Check if the character is a digit
            var digitIndex = parseInt(string[i]);
            var newDigitIndex = digitIndex + rotationFactor;
            if (newDigitIndex >= 10) {
                newDigitIndex -= 10; // Wrap around if index goes beyond '9'
            }
            newString.push(newDigitIndex.toString());
        } else if (string[i].toLowerCase() === string[i]) { // Check if the character is lowercase
            var indexLower = charactersLowercased.indexOf(string[i]);
            var newIndexLower = indexLower + rotationFactor;
            if (newIndexLower >= 26) {
                newIndexLower -= 26; // Wrap around if index goes beyond 'z'
            }
            newString.push(charactersLowercased.charAt(newIndexLower));
        } else {
            // If the character is not a letter or digit, just append it as it is
            newString.push(string[i]);
        }
    }
    var rotatedString = newString.join('');
    return rotatedString;
}

var rotatedString = rotateString();
console.log("Rotated string:", rotatedString);
