from itertools import zip_longest
from itertools import starmap

def objedini(arg1:list, arg2:list):
    return list(starmap(lambda x, y: ((x, y) if x < y else (y, x)), zip_longest(arg1, arg2, fillvalue = 0)))

print(objedini([1, 7, 2, 4, 5], [2, 5, 2]))