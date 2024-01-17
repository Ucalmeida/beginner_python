# if, elif e else

# exemplo de "if"
idade = 17
print("Exemplo de comando if")
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente.")
else:
    print("Você é menor de idade.")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)

# Entrada de dados
nova_idade = int(input("Quantos anos você tem? "))
if nova_idade >= 18:
    print("Você é maior de idade.")
elif nova_idade >= 12:
    print("Você é um adolescente.")
else:
    print("Você é menor de idade.")

outra_mensagem = "Pode tirar a carteira de habilitação" if nova_idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(outra_mensagem)
