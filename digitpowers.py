from __future__ import print_function

def dig_pow(num, pow_):
    total = 0

    for index, i in enumerate(str(num)):
        total += int(i) ** (pow_ + index)

    return total / num if total % num == 0 else -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
