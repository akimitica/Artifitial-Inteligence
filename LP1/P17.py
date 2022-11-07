from functools import reduce

def kreiraj(arg : int):
    return list(map(lambda x: (x, reduce(lambda a,b: a + b, range(0,x+1)) ** 2), range(0,arg+1)))

print(kreiraj(4))