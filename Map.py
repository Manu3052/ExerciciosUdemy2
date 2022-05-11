def dobro(x):
    return x * 2

lista = [1, 4, 6, 8, 10, 13]

valor_dobrado = map(dobro, lista)

for v in valor_dobrado:
    print(v)