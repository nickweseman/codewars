from __future__ import print_function

def delete_nth(order, max_e):
    new_order = []

    for num in order:
        if new_order.count(num) < max_e:
            new_order.append(num)
    return new_order


print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
