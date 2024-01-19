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
