def dig_pow(n, p):
    total = 0

    for index, i in enumerate(str(n)):
        total += int(i) ** (p + index)

    return total / n if total % n == 0 else -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
