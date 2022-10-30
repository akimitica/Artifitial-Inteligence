##1.a

def parni(arg):
    i=0
    for x in arg:
        if x % 2 == 0:
            i=i+1
    print(i)
    return i



##1.b

def poredak(arg1, arg2):
    
    kraca = arg1 if len(arg1) < len(arg2) else arg2
    kraca.extend([0] * abs(len(arg1) - len(arg2)))
    list3 = map(lambda x, y: (x, y, 'Jeste' if y == 2 * x else 'Nije'), arg1, arg2)
    print(list(list3))
    return list(list3)

    

list1=[1,2,3,4,8]
list2=[2,4,1,5,3]

##parni(list1)
poredak(list1,list2)