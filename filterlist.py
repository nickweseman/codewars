from __future__ import print_function


def filter_list(list_):
    return [c for c in list_ if not isinstance(c, str)]


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
