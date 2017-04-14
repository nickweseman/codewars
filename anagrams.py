from __future__ import print_function


def anagrams(word, words):
    return [item for item in words if sorted(word) == sorted(item)]

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
