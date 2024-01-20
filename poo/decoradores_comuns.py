# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10  # Atributo da classe

    def __init__(self, nome) -> None:
        self.nome = nome  # Atributo da INSTÂNCIA

    # Requer uma instância para ser chamado - Método da INSTÂNCIA
    def metodo_instancia(self):
        return f'Método de instancia chamado para {self.nome}'

    @classmethod
    def metodo_da_classe(cls):  # Usando o decorador de classe, uso o 'cls'
        # O cls recebe a classe. Dessa forma temos acesso aos atributos e métodos da CLASSE
        # O cls não permite o acesso aos atributos e métodos da INSTÂNCIA
        return f'Método da classe chamado para valor={cls.valor}'

    @staticmethod
    def metodo_estatico():
        return 'Método estático chamado'


obj = MinhaClasse(nome='Classe Exemplo')
print(obj.metodo_instancia())
# Para acessar os atributos de uma classe eu não preciso de uma instância
print('Atributo Valor:', MinhaClasse.valor)
print(MinhaClasse.metodo_da_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(',')
        return cls(marca, modelo, int(ano))


configuracao1 = 'Toyota,Corola, 2022'
carro1 = Carro.criar_carro(configuracao1)
print(f'Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}')


class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b


print(Matematica.somar(a=10, b=15))
