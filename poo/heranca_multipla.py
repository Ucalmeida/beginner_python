class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass


class Mamifero(Animal):
    def amamentar(self):
        return f'{self.nome} está amamentando'


class Ave(Animal):
    def voar(self):
        return f'{self.nome} está voando'


# Exemplo de Herança Múltipla - Ficar atento ao uso do super()
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        super().emitir_som()
        return 'Morcegos emitem sons ultrassônicos'


foca = Mamifero(nome='Furlipa')
print(foca.amamentar())
pardal = Ave(nome='Pardal')
print(pardal.voar())
batman = Morcego(nome='Zefinho')
print(batman.emitir_som())

