fib_dict = {0: 0,
            1: 1}


def productFib(prod):
    for i in range(prod):
        total = fib(i) * fib(i + 1)

        if total == prod:
            return [fib(i), fib(i + 1), True]
        elif total > prod:
            return [fib(i), fib(i + 1), False]


def fib(n):
    if fib_dict.get(n) is not None:
        return fib_dict.get(n)
    else:
        fib_dict[n] = fib_dict.get(n-1) + fib_dict.get(n-2)
        return fib_dict[n]

print(productFib(4895))
print(productFib(5895))