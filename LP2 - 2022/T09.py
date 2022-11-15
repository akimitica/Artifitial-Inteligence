from functools import reduce

def zamena(arg1, arg2):
   return list(map(lambda x, i: (x if x > arg2 else reduce(lambda a, b: (a + b), arg1[i+1:])), arg1, range(len(arg1))))

print(zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))