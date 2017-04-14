from __future__ import print_function

from collections import Counter

def scramble(text, word):
    text_dict = Counter(text)

    for letter in word:
        if letter in text_dict and text_dict[letter] != 0:
            text_dict[letter] -= 1
        else:
            return False
    return True

print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
