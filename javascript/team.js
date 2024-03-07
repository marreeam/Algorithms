// One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests.
// Participants are usually offered several problems during programming contests.
// Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution. 
// Otherwise, the friends won't write the problem's solution.

// This contest offers n problems to the participants.
// For each problem we know, which friend is sure about the solution.
// Help the friends find the number of problems for which they will write a solution.








function numberOfSolutions() {
    // Generate a random number of tasks (between 1 and 10)
    var numberOfTasks = Math.floor(Math.random() * 10) + 1;

    // Initialize a variable to store the number of tasks with two or three solutions
    var number = 0;

    // Loop through each task
    for (var i = 0; i < numberOfTasks; i++) {
        // Generate random solutions for Petya, Vasya, and Tonya (0 or 1)
        var Petya = Math.floor(Math.random() * 2);
        var Vasya = Math.floor(Math.random() * 2);
        var Tonya = Math.floor(Math.random() * 2);

        // Check if the sum of solutions equals 2 or 3
        if (Petya + Vasya + Tonya === 3 || Petya + Vasya + Tonya === 2) {
            // If yes, increment the count
            number += 1;
        }
        // No need for else-if conditions for sum === 1 or sum === 0 since they don't affect the count
    }
    // Return the total number of tasks with exactly two or three solutions
    return number;
}
var result = numberOfSolutions();
console.log(`the number of problems for which they will write a solution is : ${result}`); // This will print the value returned by the function


