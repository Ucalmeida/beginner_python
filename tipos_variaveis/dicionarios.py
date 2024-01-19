# Criando um dicionário de exemplo
pessoa = {
    "nome": "Urian",
    "idade": 46,
    "cidade": "Aracaju"
}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
pessoa["sobrenome"] = "Almeida"  # Atribuindo chave-valor a um dicionário
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionário de exemplo com sobrenome:", pessoa)

pessoa["idade"] = 50
print("Idade Atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo com sobrenome excluído:", pessoa)

# Métodos: keys(), values(), items()
chaves = pessoa.keys()  # Aparece como dict_keys
print("Chaves do meu dicionário sem cast para list:", chaves)
chaves = list(pessoa.keys())  # Fazendo cast para list
print("Primeira chave, após o cast para list:", chaves[0])  # Precisa fazer o cast para list se quiser acessar cada chave individualmente

# Método values
valores = pessoa.values()
print("Valores dos dicionários sem cast para list:", valores)  # Aparece como dict_values
# Para aparecer como foi feito com as chaves, também fazer o cast para list
valores = list(pessoa.values())
print("Valores dos dicionários com cast para list:", valores)
print("Primeiro valor do dicionário após o cast para list:", valores[0])

# Método items
itens = pessoa.items()
# Para visualizar todos os pares chave-valor que temos
print("Pares chave-valor do dicionário:", itens)
# Fazendo o cast para list
itens = list(pessoa.items())
print("Primeiro valor, após o cast para list: %s | %s", (itens[0][1], itens[1][1]))
