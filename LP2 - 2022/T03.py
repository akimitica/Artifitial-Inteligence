from itertools import *
def spoji(arg1:list, arg2:list):
    return list(starmap(lambda x, y: ( (x, y, x + y) if x < y else (y, x, x + y)), zip_longest(arg1, arg2,fillvalue = 0)))

print(spoji([1, 7, 2, 4], [2, 5, 2]))