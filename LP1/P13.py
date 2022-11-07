from functools import reduce

##13.a

def izmeni(arg):
    return list(map(lambda x, i: x + 1 if i%2==0 else x - 1, arg, range(len(arg))))

print(izmeni([8, 5, 3, 1, 1]))


##13.b

def dodaj(arg1, arg2):
    short = arg1 if len(arg1) < len(arg2) else arg2
    short.extend([0] * abs(len(arg1) - len(arg2)))
    return list(map(lambda x, y: x + y, arg1, arg2))


def skupi(arg):
    return list(map(lambda x, i: dodaj(x, arg[i + 1]), arg, range(len(arg) - 1)))

print(skupi([[1, 3, 5],[2, 4, 6],[1, 2]]))