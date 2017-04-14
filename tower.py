from __future__ import print_function


def tower_builder(n_floors):
    list_ = []

    width = 1
    for _ in range(2, n_floors + 1):
        width += 2

    num_stars = 1
    for _ in range(1, n_floors + 1):
        list_.append('{s:{c}^{n}}'.format(s='*' * num_stars, n=width, c=''))
        num_stars += 2

    return list_


print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(4))
print(tower_builder(5))

print('{s:{c}^{n}}'.format(s='*', n=5, c=''))
