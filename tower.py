def tower_builder(n_floors):
    l = []

    width = 1
    for i in range(2, n_floors + 1):
        width += 2

    num_stars = 1
    for i in range(1, n_floors + 1):
        l.append('{s:{c}^{n}}'.format(s='*' * num_stars, n = width , c = ''))
        num_stars += 2

    return l

print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(4))
print(tower_builder(5))

print('{s:{c}^{n}}'.format(s='*', n = 5, c = ''))