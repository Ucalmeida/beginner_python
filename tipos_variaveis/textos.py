# Declaração
nome_completo = "Urian Almeida"

# Com 3 aspas
nome_completo_aspas = """Urian
Almeida"""

# Com quebra \
nome_completo_quebra = "Urian \
Almeida"

# Separadas
nome = "Urian"
sobrenome = "Almeida"

# Formatação
# Forma 1
print("Nome completo:", nome_completo)

# Forma 2
print("Nome completo2: ", nome_completo)  # Ficar atento aos espaços

# Forma 3
print("Nomes Separados: " + nome + " " + sobrenome)

# Forma 4
print("Nomes Separados2:", nome, sobrenome)

# Fomra 5
print("Nome completo Aspas triplas:", nome_completo_aspas)

# Forma 6
print("Nome completo com quebra:", nome_completo_quebra)

# Forma 7
print("Nome Completo (7a forma): %s" % nome_completo)

# Forma 8
print("Nome Completo (8a forma): %s %s" % (nome, sobrenome))

# Forma 9 - Letra f na frente da string
print(f"Nome Completo (9a forma): {nome} {sobrenome}")

# Forma 10 - Parecido com o nono formato, mas sem o f antes da string
# e com uso do format
print("Nome Completo (10a forma): {} {}".format(nome, sobrenome))

# Lower
minusculo = "TuDo MinusCuLo".lower()
print(minusculo)

# Upper
maiusculo = "TuDo MaIusCuLo".upper()
print(maiusculo)

# Count
print(nome_completo.count("a"))

# Find
print(nome_completo.find("a"))

# Encode
print(nome.encode())

# Decode
print(nome.encode().decode())

# Replace
print(nome_completo.replace("r", "u"))
print(nome_completo.replace("a", "v"))
telefone = "(79)99814-9831"
print(telefone)
print(telefone.replace("(", "").replace(")", "").replace("-", ""))

# Join
print("-".join("Urian"))

# Split
print(nome_completo.split(" "))

# Strip - Afeta a string no início ou no final
print("xUrian Almeidax".strip("x"))
# Right Strio - Afeta o a string no final
print("xUrian Almeidax".rstrip("x"))

# Left Strio - Afeta o a string no inicio
print("xUrian Almeidax".lstrip("x"))

# Starts With - Verifica se a string inicia com um determinado caracter
print(nome_completo.startswith("Ur"))
print(nome_completo.startswith("Ga"))

# IN e Not IN
print("ri" in nome_completo)
print("abc" in nome_completo)
print("abc" not in nome_completo)

# Multiplicar letras
muitas_letras = "XyZ" * 100
print(muitas_letras)

# Substituir Letras
substituicao = "algomania".replace("mania", "maluco")
print(substituicao)
