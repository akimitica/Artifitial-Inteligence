from functools import reduce

##8.a

def izmeni(arg):
    for x in range (1,len(arg)):
        arg[x]+=arg[x-1]
    return arg

print(izmeni([1, 2, 4, 7, 9]))


##8.b

def izracunaj(arg):
    return list(map(lambda x : x if type(x) in {int, float} else reduce(lambda x,y: x * y, x), arg))


print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))