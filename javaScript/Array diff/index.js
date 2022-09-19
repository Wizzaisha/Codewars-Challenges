function arrayDiff(a, b) {
    
    return a.filter(element => {
        return b.indexOf(element) === -1;
    })


}


const arrA = [1,2,2];
const arrB = [1];

console.log(arrayDiff(arrA, arrB));