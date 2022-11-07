##7.a

def operacija(arg1, arg2):
    
    return list(map(arg2, arg1, arg1))

print(operacija([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y))