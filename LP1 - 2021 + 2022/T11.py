from functools import reduce

##11.a

def razlika(arg):
    return list(map(lambda x, i: x - arg[i + 1], arg, range(len(arg)-1)))

print(razlika([8, 5, 3, 1, 1]))


##11.b

def proizvod(arg):
    return reduce(lambda x, y: x * (y if type(y) in {int, float} else proizvod(y)), arg, 1)


print(proizvod([[1, 3, 5], [2, [2, [2, 2]], 6], [1, 2, 3]]))