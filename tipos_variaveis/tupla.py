# Ordenada e IMUTÁVEL(Diferente da Lista)
minha_tupla = (1, 2, 2, 3, 4)
print("Minha Tupla:", minha_tupla)

# Exibindo a lista
print("Minha lista de exemplo", minha_tupla)

# Exibindo a lista por índice
print("minha_tupla[0]:", minha_tupla[0])
print("minha_tupla[2]:", minha_tupla[2])
print("minha_tupla[-1]:", minha_tupla[-1])

# Slice - Fatiamento - Exibindo os elementos de uma lista
print("minha_tupla[1:7]:", minha_tupla[1:7])  # Do segundo elemento até o sexto
print("minha_tupla[:6]:", minha_tupla[:6])  # Até o quinto elemento
print("minha_tupla[2:]:", minha_tupla[2:])  # Do terceiro elemento em diante

# Método count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

# Método index
indice = minha_tupla.index(2)
print("Índice da PRIMEIRA ocorrência do elemento 2:", indice)
