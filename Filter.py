#Não pythonico
#lista = [1,2,3,4,5,6,7,8,9,10,20,34,25,67]

#for i in lista:
    #if i%2 ==0:
        #print(i)


#Método pynthonico

def par(i):
    if i % 2== 0:
        return i

def impar(i):
    if i % 2 != 0:
        return i

lista = [1,2,3,4,5,6,7,8,9,10,25,34,90,237]

lista_pares = filter(par, lista)
lista_impar = filter(impar, lista)

print(list(lista_pares))
print(list(lista_impar))
