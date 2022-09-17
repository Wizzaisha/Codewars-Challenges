function order(words){
    // ...
    if (words.length === 0) return words;

    let arr = words.split(" ");

    arr.sort((a, b) => a.match(/\d+/g) - b.match(/\d+/g))

    return arr.join(" ");
}


let str1 = "is2 Thi1s T4est 3a";
let str2 = "4of Fo1r pe6ople g3ood th5e the2";
let str3 = "";

console.log(order(str1));
console.log(order(str2));
console.log(order(str3));