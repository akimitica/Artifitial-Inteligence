from functools import reduce

def proizvod(arg1, arg2):
    return list(map(lambda x, y: (y * reduce(lambda i, j: (i + j), x)), arg1, arg2))

print(proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]))


