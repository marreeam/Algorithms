// You are given three integers 𝑎, 𝑏, and 𝑐. Determine if one of them is the sum of the other two.




function isSum(x, y, z) {
    const sumOfXY = x + y;
    const sumOfXZ = x + z;
    const sumOfYZ = y + z;
    const listOfSums = [sumOfXY, sumOfXZ, sumOfYZ];
    for (let i = 0; i < 3; i++) {
        if (x === listOfSums[i]) {
            return "X is the sum of the other two.";
        } else if (y === listOfSums[i]) {
            return "Y is the sum of the other two.";
        } else if (z === listOfSums[i]) {
            return "Z is the sum of the other two.";
        }
    }
    return "Neither of them is the sum of the other two.";
}

console.log(isSum(2, 4, 2)); // Output: "Y is the sum of the other two."
