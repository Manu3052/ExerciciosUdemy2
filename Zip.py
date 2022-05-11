#Concatenação de listas

lista1 = [1, 2, 3, 4, 5]
lista2 =["Mamão", "abacate", "jiló", "uva", "salsinha"]
lista3 = [ "R$ 2,00", "R$ 10,00", "R$ 7,00", "R$ 3,00", "R$ 1,50"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)