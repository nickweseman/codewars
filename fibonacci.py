from __future__ import print_function

FIB_DICT = {0: 0,
            1: 1}


def product_fib(prod):
    for i in range(prod):
        total = fib(i) * fib(i + 1)

        if total == prod:
            return [fib(i), fib(i + 1), True]
        elif total > prod:
            return [fib(i), fib(i + 1), False]


def fib(n):
    if FIB_DICT.get(n) is not None:
        return FIB_DICT.get(n)

    FIB_DICT[n] = FIB_DICT.get(n - 1) + FIB_DICT.get(n - 2)
    return FIB_DICT[n]

print(product_fib(4895))
print(product_fib(5895))
