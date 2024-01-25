from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        return 'Carro ligado'

    def desligar(self):
        return 'Carro desligado'


carro = Carro()
print(carro.ligar())
print(carro.desligar())
