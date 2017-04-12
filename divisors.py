def divisors(integer):
    list_ = [i for i in range(2, integer) if integer % i == 0]

    if list_:
        return list_
    else:
        return "{} is prime".format(integer)

print(divisors(15))
print(divisors(12))
print(divisors(13))