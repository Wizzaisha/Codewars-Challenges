function DNAStrand(dna){
    //your code here

    let newArr = [...dna].map(element => {
        switch (element) {
            case "A":
                return "T"
            case "T":
                return "A"
            case "G":
                return "C"
            case "C":
                return "G"
        }
    })

    return newArr.join("");

}



const chain1 = "AAAA";
const chain2 = "ATTGC";
const chain3 = "GTAT";

console.log(DNAStrand(chain1));
console.log(DNAStrand(chain2));
console.log(DNAStrand(chain3));