class Pessoa:
    olhos = 2

    def __init__(self, *irmaos, nome = None, idade = 17):
        self.idade = idade
        self.nome = nome
        self.irmaos = list(irmaos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    elton = Homem(nome = 'elton')
    oscar = Mutante(elton, nome = 'oscar')
    elton = Homem(oscar, nome = 'elton')
    print(Pessoa.cumprimentar(oscar))
    print(id(oscar))
    print(oscar.cumprimentar())
    print(oscar.nome)
    print(oscar.idade)
    for irmao in elton.irmaos:
        print(irmao.nome)
    for irmao in oscar.irmaos:
        print(irmao.nome)
    oscar.sobrenome = 'borges'
    elton.sobrenome = 'faletinha'
    elton.idade = 25
    del elton.sobrenome
    oscar.olhos = 1
    del oscar.olhos
    print(oscar.__dict__)
    print(elton.__dict__)
    print(Pessoa.olhos)
    print(oscar.olhos)
    print(elton.olhos)
    print(id(Pessoa.olhos), id(elton.olhos), id(oscar.olhos))
    print(Pessoa.metodo_estatico(), oscar.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), oscar.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(oscar, Pessoa))
    print(isinstance(oscar, Homem))
    print(oscar.olhos)
    print(oscar.cumprimentar())
    print(elton.cumprimentar())
