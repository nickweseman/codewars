def breakChocolate(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return (n - 1) + ((m - 1) * n)

print(breakChocolate(5, 5))
print(breakChocolate(2, 1))
print(breakChocolate(3, 1))
print(breakChocolate(2, 2))
print(breakChocolate(3, 3))
print(breakChocolate(1, 1))
print(breakChocolate(1, -1))
print(breakChocolate(-55, 1))
