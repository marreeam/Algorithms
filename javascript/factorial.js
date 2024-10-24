function factorial(n){
    let factorial=1;
    while(n>0){
        factorial*=n;
        n-=1
    }
    console.log(factorial)
}
factorial(9)