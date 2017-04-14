from __future__ import print_function

import string

def dna_strand(dna):
    map_ = string.maketrans("ATCG", "TAGC")

    return dna.translate(map_)

print(dna_strand("AAAA"))
print(dna_strand("ATTGC"))
print(dna_strand("GTAT"))
