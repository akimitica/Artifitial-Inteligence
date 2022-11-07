from functools import reduce

##9.a

def prosek(arg):
    return list(map(lambda x: reduce(lambda y, z : y + z, x)/len(x),arg))

#print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))


##9.b

def zameni(arg1, arg2):
    return list(map(lambda x, i: x if x > arg2 else reduce(lambda a, b: a + b, arg1[i+1:]), arg1, range(len(arg1))))

print(zameni([1,7,5,4,9,1,2,7],5))