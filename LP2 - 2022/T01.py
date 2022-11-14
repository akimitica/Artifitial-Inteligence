def poredak(arg1:list, arg2:list):
    kraca = arg1 if len(arg1) < len(arg2) else arg2
    kraca.extend([0] * abs(len(arg1) - len(arg2))) 
    return list(map(lambda x, y: (x, y, 'Jeste' if y==2 * x else 'Nije'), arg1, arg2))

print(poredak([1, 7, 2, 4], [2, 5, 2]))