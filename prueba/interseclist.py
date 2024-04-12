def intersect(lista1, lista2):
    lista3=[]

    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]==lista2[j]:
                lista3.append(lista1[i])

    return lista3

lista1=[3,4,5,6,7]
lista2=[1,2,3,4,5]
print(intersect(lista1, lista2))