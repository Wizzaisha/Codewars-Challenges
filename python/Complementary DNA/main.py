def DNA_strand(dna):
    # code here
    result = list(map(lambda x: "T" if x == "A" else "A" if x == "T" else "G" if x == "C" else "C", list(dna)))
    return "".join(result)


dna1 = "AAAA"
dna2 = "ATTGC"
dna3 = "GTAT"

print(DNA_strand(dna1))
print(DNA_strand(dna2))
print(DNA_strand(dna3))