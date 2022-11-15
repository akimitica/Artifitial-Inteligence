def stepen(arg):
    return list(map(lambda i:(arg[i]**arg[i+1]), range(len(arg)-1)))

print(stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]))