# Princípios e Conceitos: POO:: É um paradigma de programação
# que se baseia na organização dos programas em torno de Objetos
# Objetos são instâncias de Classes

# Classe:: É um modelo. Um plano que define
# a estrutura e o comportamento de um objeto
# Podemos lembrar aqui de uma Blueprint

# Classe de exemplo:: Temos dentro de nossas classes
# descrição de nossos atributos, que são basicamente
# propriedades dessas classes, e os métodos que são
# as ações, o comportamento, define o que os objetos
# criados a partir dessa classe poderão fazer
class Pessoa:
    # __init__ é o método construtor do Python
    # Essa função, quando em uma classe
    # passa a se chamar:: Método - Ou seja:
    # Método é uma Função declarada em uma Classe
    # self é uma Referência a própria Classe

    # Uma referência funciona como uma porta de acesso
    # para poder utilizar os métodos e atributos
    # de uma classe
    # -> None: funciona como uma dica e indica que o método não tem retorno
    # Não é obrigatório
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.'


# Objeto:: Instâncias concretas de uma classe,
# que podem representar entidades do mundo real
pessoa1 = Pessoa('Antonio', 35)
print('Referência:', pessoa1)  # Exibe o número da referência do Objeto
print('Nome:', pessoa1.nome)
print('Idade:', pessoa1.idade)
print(pessoa1.saudacao())

pessoa2 = Pessoa(nome="Rodrigo", idade=42)
print('Referência2:', pessoa2)
print(pessoa2.saudacao())

# Pilares do POO: Encapsulamento, Herança, Polimorfismo e Abstração 
