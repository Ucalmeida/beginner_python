# Funções:: Bloco de código reutilizável
def saudacao(nome):
    print(f"Olá, {nome}!")


print("\nChamando a Função saudacao():")
saudacao("Urian")
saudacao("Bob")


# Funçào com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado


print("\nChamando a Função quadrado():")
numero_fornecido = int(input("Digite um valor: "))
resultado_quadrado = quadrado(numero_fornecido)
print(f"O quadrado de {numero_fornecido} é", resultado_quadrado)


# Função com múltiplos parâmetros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


print("\nChamando a Função soma():")
primeiro_numero = int(input("Digite um valor: "))
segundo_numero = int(input("Digite mais um valor: "))
resultado_soma = soma(primeiro_numero, segundo_numero)
print(f"Primeira forma de imprimir os resultados:: A soma {primeiro_numero} + {segundo_numero} é {resultado_soma}")
print(f"Segunda forma de imprimir os resultados:: A soma {primeiro_numero} + {segundo_numero} é ", resultado_soma)
print("Terceira forma:: A soma %s + %s é %s" % (primeiro_numero, segundo_numero, resultado_soma))
print("Aqui no console vai estar tudo igual, mas no código não")

# 
