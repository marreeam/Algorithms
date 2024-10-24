function fibonacchi(N) {
    const fibonacchiLenght = 40;
    const fibonacchiList = [0, 1];
    for (var i = 2; i < fibonacchiLenght; i++) { 
        fibonacchiList.push(fibonacchiList[i - 2] + fibonacchiList[i - 1]);
    }
  
    
}

fibonacchi(); 

