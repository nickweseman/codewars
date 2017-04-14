from __future__ import print_function

def order(sentence):
    words = sentence.split()

    return " ".join(sorted(words, key=find_num))


def find_num(str_):
    for c in str_:
        if str.isdigit(c):
            return int(c)

print(order("is2 Thi1s T4est 3a"))
