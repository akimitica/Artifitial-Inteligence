##6.a

def razlika(arg1,arg2):
    res = [] * len(arg1)
    for x in arg1:
        if x not in arg2:
            res.append(x)
    return res

#print (razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))


##6.b

def objedini(arg1,arg2):
    kraci = arg1 if len(arg1) < len(arg2) else arg2
    kraci.extend([0] * abs( len(arg1) - len(arg2)))

    ##return list(zip(arg1,arg2))

    return list(map(lambda x,y:(x,y) if x<y else (y,x),arg1,arg2))


print(objedini([1, 7, 2, 4, 5], [2, 5, 2]) )