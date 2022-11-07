##3.a

def uredi(args,nElem,val):
    for x in range(nElem):
        args[x]+=val
    for x in range(nElem, len(args)):
        args[x]-=val
    print(args)


uredi([1, 2, 3, 4, 5], 3, 1)


##3.b

def spoji(arg1,arg2):
    kraci = arg1 if len(arg1) < len(arg2) else arg2
    kraci.extend([0] * abs(len(arg1)  - len(arg2)))

    res= map(lambda x,y: (x, y, x + y), arg1, arg2)

    return list(res)