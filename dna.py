import string

def DNA_strand(dna):
    map = string.maketrans("ATCG", "TAGC")

    return dna.translate(map)

print(DNA_strand("AAAA"))
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))