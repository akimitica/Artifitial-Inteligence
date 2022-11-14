from itertools import starmap, zip_longest

def spojidict(arg1:list, arg2:list):
    return list(starmap(lambda x, y: {'Prvi': x, 'Drugi': y}, zip_longest(arg1,arg2, fillvalue = '-')))


print(spojidict([1, 7, 2, 4], [2, 5, 2]))