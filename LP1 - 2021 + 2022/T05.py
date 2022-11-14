##5.a

def brojel(arg):
    res=[None] * len(arg)
    for x in range(len(arg)):
        res[x]=len(arg[x]) if type(arg[x]) is list else -1
    return res

##print(brojel([[1, 2], [3, 4, 5], 'el', ['1', 1]]))


##5.b

def proizvod(arg1,arg2):
    res = [None] * len(arg2)
    
    for x in range(len(arg1)):
        sum=0
        for y in range(len(arg1[x])):
            sum+=arg1[x][y]
        res[x]=sum*arg2[x]
    return list(res)

print(proizvod([[1,2,3],[4,5,6],[7,8,9]], [1,2,3]))