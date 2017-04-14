from __future__ import print_function

from fractions import gcd


def convertFracts(list_):
    lcm = list_[0][1]

    for fract in list_[1:]:
        lcm = get_lcm(lcm, fract[1])

    return [[fract[0] * (lcm / fract[1]), fract[1] * (lcm / fract[1])]
            for fract in list_]

def get_lcm(x, y):
    return (x * y) // gcd(x, y)

a = [[1, 2], [1, 3], [1, 4]]
b = [[6, 12], [4, 12], [3, 12]]

c = [[69, 130], [87, 1310], [3, 4]]

d = [[27115, 5262], [87546, 11111111], [43216, 255689]]

print(convertFracts(a))
print(convertFracts(c))
print(convertFracts(d))
