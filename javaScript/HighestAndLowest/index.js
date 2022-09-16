function highAndLow(numbers){
    // ...
    let numInt = numbers.split(" ");

    numInt.sort((a, b) => a - b);

    console.log(numInt);

    return `${numInt[numInt.length - 1]} ${numInt[0]}`

}


const numbersStr = "8 3 -5 42 -1 0 0 -9 4 7 4 -4";
const numbersStr2 = "1 2 3";

console.log(highAndLow(numbersStr));
console.log(highAndLow(numbersStr2));