def is_prime(num):
    num = abs(num)

    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True




print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(57))
