class Pessoa:
    def __init__(self, *irmaos, nome = None, idade = 17):
        self.idade = idade
        self.nome = nome
        self.irmaos = list(irmaos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    elton = Pessoa( nome = 'elton')
    oscar = Pessoa(elton, nome = 'oscar')
    print(Pessoa.cumprimentar(oscar))
    print(id(oscar))
    print(oscar.cumprimentar())
    print(oscar.nome)
    print(oscar.idade)
    for irmaos in oscar.irmaos:
        print(irmaos.nome)
