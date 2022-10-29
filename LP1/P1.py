def parni(lista):
    i=0
    for x in lista:
        if x % 2 == 0:
            i=i+1
    print(i)


def poredak(lista1,lista2):
    
    if lista1.size()!=lista2.size():
        print(printlista)
    else:
        list3.append(lista1.pop)
        list3.append(lista2.pop)
        if list3[0]>list3[1]:
            list3.append('Nije')
        else:
            list3.append('Jeste')
        printlista.append(list3)
        poredak(lista1,lista2)



lista=[1,2,3,4,5,6,8]
parni(lista)