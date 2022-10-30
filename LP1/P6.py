##6.a

def razlika(arg1,arg2):
    res = [] * len(arg1)
    for x in arg1:
        if x not in arg2:
            res.append(x)
    return res

print (razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))


##6.b

#def objedini(arg1,arg2):