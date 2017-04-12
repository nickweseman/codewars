def filter_list(l):
    return [c for c in l if not isinstance(c, str)]

print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))