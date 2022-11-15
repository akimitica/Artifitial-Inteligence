from functools import reduce

def izracunaj(arg):
    return list(map(lambda x: (x if type(x) in (int, float) else reduce(lambda i, j: (i * j), x)), arg))



print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))