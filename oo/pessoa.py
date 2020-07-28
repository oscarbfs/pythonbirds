class Pessoa:
    olhos = 2

    def __init__(self, *irmaos, nome = None, idade = 17):
        self.idade = idade
        self.nome = nome
        self.irmaos = list(irmaos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    elton = Pessoa(nome = 'elton')
    oscar = Pessoa(elton, nome = 'oscar')
    elton = Pessoa(oscar, nome = 'elton')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(oscar.olhos)
    print(elton.olhos)
    print(id(Pessoa.olhos), id(elton.olhos), id(oscar.olhos))
