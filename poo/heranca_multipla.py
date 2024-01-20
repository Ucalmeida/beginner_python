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
morcego = Morcego(nome='Batman')

# Acessando métodos da classe base 'Animal'
print('Nome de morcego:', morcego.nome)
print(morcego.emitir_som())

# Acessando métodos da classe 'Mamífero' e 'Ave'
print(f'{morcego.nome} {morcego.amamentar()}')
print(f'{morcego.nome} {morcego.voar()}')
