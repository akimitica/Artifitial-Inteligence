from functools import reduce

##12.a

def presek(arg1,arg2):
    return list(filter(lambda x: x in arg1, arg2))

print(presek([1, 5, 4, "1", "8", 3, 7], [1, 9, "1"]))


##12.b

def izracunaj(arg):
    return list(map(lambda x: x ** 2 if type(x) in {int, float} else reduce(lambda x,y: x**2 + y**2, x), arg))

print(izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]) )