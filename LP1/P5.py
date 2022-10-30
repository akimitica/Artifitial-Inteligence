##5.a

def brojel(arg):
    res=[None] * len(arg)
    for x in range(len(arg)):
        res[x]=len(arg[x]) if type(arg[x]) is list else -1
    return res

print(brojel([[1, 2], [3, 4, 5], 'el', ['1', 1]]))


##5.b

##def proizvod(arg1,arg2):