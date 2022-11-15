from functools import reduce

#def objedini(arg:list):
#    return reduce(lambda x,y: dodajnaprvo(a, b), list(map(lambda x: {x:None} if type(x) in (int, float))))

def objedini(arg):
    listaDict = list(map(lambda a: {a[0]: list(a[1:])} if (type(a) is tuple) else {a: None}, arg))
    return {list(x.keys())[0]: x.get(list(x.keys())[0]) for x in listaDict}