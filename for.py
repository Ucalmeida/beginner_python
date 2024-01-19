#
print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

print("\nFor utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "Joao", "idade": 30, "cidade": "Aracaju"}
print("\nFor utilizando dicionario - chaves")
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utilizando dicionario - items")
for chave, valor in pessoa.items():
    print(f"{chave} - {valor}")

# range(): intervalo numérico
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nRange convertido em uma lista")
print(list(range(0, 10)))

print("\nUtilizando a função range()")
for numero in range(5):
    print("Número:", numero)

print("\nUtilizando a função range() com len()")
nova_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Antes do FOR:", nova_lista)
for indice in range(0, len(nova_lista)):
    print("Índice:", indice)
    print("Elemento:", nova_lista[indice])
    if indice == 3:
        nova_lista[indice] = 10
print("Após o FOR:", nova_lista)

# enumerate()
lista_enumerate = ["apple", "banana", "cherry"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Era Banana!")
