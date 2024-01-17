minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo a lista por índice
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])

# Slice - Fatiamento - Exibindo os elementos de uma lista
print("minha_lista[1:7]:", minha_lista[1:7])  # Do segundo elemento até o sexto
print("minha_lista[:6]:", minha_lista[:6])  # Até o quinto elemento
print("minha_lista[2:]:", minha_lista[2:])  # Do terceiro elemento em diante

# Reatribuir elemento
minha_lista[0] = "python"
print("Minha lista elemento[0] reatribuído:", minha_lista)

# Método append(): Adiciona um elemento ao final de uma lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Índice do Elemento 6:", indice)

# Método Insert: Insere um elemento em um índice específico e desloca os elementos originais para a direita
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista)

# Método pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3):", minha_lista)

# Método remove
minha_lista.remove(True)
print("Após o remove(True):", minha_lista)

# Método sort; Ordem crescente
minha_lista_numeros = [4, 5, 8, 1, 9, 3]
minha_lista_numeros.sort()
print("Após o sort():", minha_lista_numeros)

