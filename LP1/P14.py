from functools import reduce

##14.a

def unija(arg1,arg2):
    return list(reduce(lambda x, y: x if y not in x and x.append(y) else x, arg2, arg1))

print(unija([5, 4, "1", "8", 3, 7], [1, 9, "1"]))


##14.b

def suma(arg, i = 0):
    if type(arg[i]) == int:
        return arg[i] + (suma(arg, i + 1) if len(arg) > i + 1 else 0)
    elif type(arg[i]) is list:
        return suma(arg[i], 0) + (suma(arg, i + 1) if len(arg) > i + 1 else 0)