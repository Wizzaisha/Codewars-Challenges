function pigIt(str){
    //Code here

    let newStr = str.split(" ").map(e => {
        let letterArr = [...e];
        
        let first = letterArr[0];
        let last = letterArr[letterArr.length]

        letterArr[0] = last;
        letterArr[letterArr.length] = first;

        const symbols = /^[!@#?\$%\^\&*\)\(+=._-]+$/g;

        return symbols.exec(letterArr.join("")) ? letterArr.join("") : letterArr.join("") + "ay";

    })
    return newStr.join(" ");
}


const str1 = "Pig latin is cool";
const str2 = "Hello world !";

console.log(pigIt(str1));
console.log(pigIt(str2));