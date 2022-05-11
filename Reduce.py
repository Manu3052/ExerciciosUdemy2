from functools import reduce

def soma(x, y):
    return x+y

lista = [2,7,8,10]

soma = reduce(soma, lista)
print(soma)
