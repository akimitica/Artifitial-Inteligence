from functools import reduce

def izracunaj(arg):
    return list(map(lambda x: (x**2 if type(x) == int else reduce(lambda a, b: (a + b**2), x, 0)), arg))


print(izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]))