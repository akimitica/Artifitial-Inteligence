##2.a

def numlista(arg):
    ret=[]
    for x in arg:
        if type(x) == int:
            ret.append(x)
    print(ret)


numlista(["Prvi", "Drugi", 2, 4, [3, 5]])


##2.b

def spojidict(arg1,arg2):
    kraci = arg1 if len(arg1)<len(arg2) else arg2
    kraci.extend(['-'] * abs(len(arg1) - len(arg2)))


    arg1=list(dict('Prvi', arg1))
    arg2=list(dict('Drugi', arg2))
    res = list(zip(arg1, arg2))
    return res