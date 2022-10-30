##4.a

def zbir(arg):
    res=arg.copy()
    res.pop()
    for x in range(len(arg) - 1):
        res[x] = res[x] + arg[x + 1]
    
    print(res)
    return res

zbir([1, 2, 3, 4, 5])



##4.b

def suma(arg, i = 0):
    if type(arg[i]) == int:
        return arg[i] + (suma(arg, i + 1) if len(arg) > i + 1 else 0)
    elif type(arg[i]) is list:
        return suma(arg[i], 0) + (suma(arg, i + 1) if len(arg) > i + 1 else 0)


print(suma([1, 1, [1, [1, [1, [[1]]]]], 1, [1, 1, [1, 1]]]))