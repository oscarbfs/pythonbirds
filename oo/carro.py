class Motor:
    v = 0
    def velocidade(self):
        print(self.v)

    def acelerar(self):
        self.v += 1

    def frear(self):
        self.v -= 2

class Direcao:
    direcao = 'Norte'

    def valor(self):
        print(self.direcao)

    def girar_para_a_direita(self):
        if self.direcao == 'Norte':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Norte'

    def girar_para_a_esquerda(self):
        if self.direcao == 'Norte':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Norte'

class Carro(Motor, Direcao):
    pass


motor = Carro()
motor.velocidade()
motor.acelerar()
motor.velocidade()
motor.acelerar()
motor.velocidade()
motor.frear()
motor.velocidade()

direcao = Carro()
direcao.valor()
direcao.girar_para_a_direita()
direcao.valor()
direcao.girar_para_a_direita()
direcao.valor()
direcao.girar_para_a_direita()
direcao.valor()
direcao.girar_para_a_direita()
direcao.valor()
direcao.girar_para_a_esquerda()
direcao.valor()
direcao.girar_para_a_esquerda()
direcao.valor()
