from __future__ import print_function


def break_chocolate(num1, num2):
    if num1 <= 0 or num2 <= 0:
        return 0
    return (num1 - 1) + ((num2 - 1) * num1)

print(break_chocolate(5, 5))
print(break_chocolate(2, 1))
print(break_chocolate(3, 1))
print(break_chocolate(2, 2))
print(break_chocolate(3, 3))
print(break_chocolate(1, 1))
print(break_chocolate(1, -1))
print(break_chocolate(-55, 1))
