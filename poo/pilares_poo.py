# Herança
print('\nExemplo de Heranças')


class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f'O animal {self.nome} andou')
        return

    def emitir_som(self):
        pass


class Cachorro(Animal):
    def emitir_som(self):
        return 'Au, au'


class Gato(Animal):
    def emitir_som(self):
        return 'Miauuu!'


# Polimorfismo:: Permite utilizar um método definido pela classe mãe
# reimplementado de outra forma. Ex:: Classes Cachorro e Gato


dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print('\nexemplo de Polimorfismo')
animais = [dog, cat]

for animal in animais:
    print(f'{animal.nome} faz: {animal.emitir_som()}')

# Terceiro conceito: Encapsulamento
print('\nExemplo de Encapsulamento')


class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo  # Dois __ torna o atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Saldo da Conta Bancária: {self.consultar_saldo()}')
        else:
            print(f'Valor precisa ser maior que o fornecido. Valor: {valor}')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saldo da Conta Bancária: {self.consultar_saldo()}')
        elif (0 >= valor):
            print(f'Valor precisa ser maior que o fornecido. Valor: {valor}')
        else:
            print(f'Saldo menor que o valor fornecido. Saldo: {self.__saldo} menor que {valor}')

    def consultar_saldo(self):
        return self.__saldo


conta = ContaBancaria(saldo=1000)
conta.depositar(valor=500)
conta.depositar(valor=-500)
conta.sacar(valor=200)
conta.sacar(valor=2000)

conta_do_zezinho = ContaBancaria(saldo=50)

# Abstração: Não pode criar objetos a partir dela - Ela é um molde
# para outras classes
print('\nExemplo de Abstração')
from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod
    def ligar(self):  # Funciona como um contrato. É obrigado definir o uso
        pass

    @abstractmethod
    def desligar(self):
        pass


# Classe Carro não pode ser instanciada
# sem os métodos ligar e desligar serem implementados
# class Carro(Veiculo):
#     def __init__(self) -> None:
#         pass
#
#
# carro_amarelo = Carro()

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return 'Carro ligado usando a chave'

    def desligar(self):
        return 'Carro desligado usando a chave'


carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
