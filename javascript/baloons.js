//task//

// In an ICPC contest, balloons are distributed as follows:

// Whenever a team solves a problem, that team gets a balloon.
// The first team to solve a problem gets an additional balloon.
// A contest has 26 problems, labelled 𝖠, 𝖡, 𝖢, ..., 𝖹
// . You are given the order of solved problems in the contest, denoted as a string 𝑠
// , where the 𝑖
// -th character indicates that the problem 𝑠𝑖
//  has been solved by some team. No team will solve the same problem twice.
// Determine the total number of balloons that the teams received. Note that some problems may be solved by none of the teams.
//-------------------------------------------------



//explanation//

//so, in case u could not understand this code firstly, like i could not, i will explain what to should in one sentence:
//you should first find out if the problem name is in the string firstly, basicly if you have ABA string, you can see that A is firstly used so
//team gets 2 baloons, B is firstly used so team gets two baloons,A is already in a sentence so team gets 1 baloon, total is 5


//what to do //
//so you should write a program which will find unique characters in your string and double its number, and other characters will be added then 
function solvedTasks() {
    var characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
   
        var solvedProblems = "";
        var numCharacters = Math.floor(Math.random() * (characters.length - 1)) + 1; // Random number of characters
        for (var j = 0; j < numCharacters; j++) {
            var randomIndex = Math.floor(Math.random() * characters.length);
            solvedProblems += characters[randomIndex];
        }
    
        return solvedProblems
         // Output the solved problems for each iteration
    }


solvedTasks();

function baloons(){
    var solvedProblems = solvedTasks(); 
    console.log(solvedProblems);
    var UniqueCharacters=[];
    UniqueCharacters.push(solvedProblems[0])
    for(var i = 0; i<solvedProblems.length;i++){
        if(!UniqueCharacters.includes(solvedProblems[i]) ){
            UniqueCharacters.push(solvedProblems[i]);
        }


    }
    console.log("Unique Characters:", UniqueCharacters.join(", "));

    var FirstlySolvedTasks = UniqueCharacters.length;
    var everyProblem = solvedProblems.length;
    var secondtime= everyProblem - FirstlySolvedTasks;
    var thetotalbaloons= FirstlySolvedTasks*2+secondtime
    console.log("total number of characters is "+thetotalbaloons)
 
   


    

}




baloons();

