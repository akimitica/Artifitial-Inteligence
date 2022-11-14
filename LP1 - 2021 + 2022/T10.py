from functools import reduce

##10.a

def izbroj(arg):
    return reduce(lambda a, b: a+(1 if type(b) in {int, float} else izbroj(b)), arg, 0)

#print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))


##10.b

def stepen(arg):
    return list(map(lambda x, i: x ** arg[i+1], arg, range(len(arg)-1)))



