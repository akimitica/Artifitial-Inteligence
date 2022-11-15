from functools import reduce

def proizvod(arg):
    return reduce(lambda x, y: x*(y if type(y) is int else proizvod(y)), arg, 1)


print(proizvod([[1, 3, 5], [2, 4, 6], [1, 2, 3]]))