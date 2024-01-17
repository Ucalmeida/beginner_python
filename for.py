print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Antes do FOR:", lista)
for indice in range(0, len(lista)):
    print("Índice:", indice)
    print("Elemento:", lista[indice])
    if indice == 3:
        lista[indice] = 10
print("Após o FOR:", lista)

# enumerate()
lista_enumerate = ["apple", "banana", "cherry"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Era Banana!")
