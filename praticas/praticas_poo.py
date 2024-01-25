class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_idade(self):
        return self.__idade

    def set_nome(self, nome):
        self.__nome = nome

    def set_sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def set_idade(self, idade):
        self.__idade = idade

    def frase(self):
        return f'{self.get_nome()} {self.get_sobrenome()}, que tem {self.get_idade()} anos, resolveu viajar'

    def imprimir_dados_pessoa(self):
        print(f'Nome: {self.get_nome()}')
        print(f'Sobrenome: {self.get_sobrenome()}')
        print(f'Idade: {self.get_idade()}')


homem = Pessoa(nome='Zezinho', sobrenome='da Ema', idade=65)
print(homem.frase())
print(homem.imprimir_dados_pessoa())
