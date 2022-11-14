def suma(arg:list, i = 0):
    if type(arg[i]) == int:
        return arg[i] + (suma(arg, i + 1) if len(arg) > i + 1 else 0)
    elif type(arg[i]) == list:
        return suma(arg[i], 0) + (suma(arg, i + 1) if len(arg) > i + 1 else 0)

print(suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))