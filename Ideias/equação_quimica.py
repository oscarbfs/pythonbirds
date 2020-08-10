# Equação de neutralização (acido + base)

atomo0 = input('Informe o primeiro atomo da primeira molecula (todos diferentes de H ou OH considerere como se todos juntos fossem um atomo só): ')
atomo0_1 = input('Informe o segundo atomo da primeira molecula (todos diferentes de H ou OH considerere como se todos juntos fossem um atomo só): ')
atomo1 = input('Informe o primeiro atomo da segunda molecula (todos diferentes de H ou OH considerere como se todos juntos fossem um atomo só): ')
atomo1_1 = input('Informe o segundo atomo da segunda molecula (todos diferentes de H ou OH considerere como se todos juntos fossem um atomo só): ')

estrutura = atomo0 + atomo0_1
estrutura1 = atomo1 + atomo1_1


class Molecula:

    def __init__(self, *tipo, tipo1 = None, formula = estrutura, formula1 = estrutura1):
        self.tipo = tipo
        self.tipo1 = tipo1
        self.formula = formula
        self.formula1 = formula1

        if self.formula[0] == 'H':
            self.tipo = 'acido'
        elif self.formula1[0] == 'H':
            self.tipo1 = 'acido'
        else:
            raise Exception('Deve haver pelo menos um ácido!')

        if self.formula[-2] + self.formula[-1] == 'OH':
            self.tipo = 'base'
        elif self.formula1[-2] + self.formula1[-1] == 'OH':
            self.tipo1 = 'base'
        else:
            raise Exception('Deve haver pelo menos uma base!')


    def reacao_quimica(self):

        if self.tipo == 'acido':
            newformula = self.formula.replace('H', '')
        elif self.tipo == 'base':
            newformula1 = self.formula.replace('OH', '')

        if self.tipo1 == 'acido':
            newformula = self.formula1.replace('H', '')
        elif self.tipo1 == 'base':
            newformula1 = self.formula1.replace('OH', '')


        if self.tipo == 'acido' and self.tipo1 == 'base' or self.tipo == 'base' and self.tipo1 == 'acido':
            print(f'Equação não balanciada da reação quimica: {self.formula} + {self.formula1} = {newformula1 + newformula} + H2O')


    def informar_o_tipo(self):
        if self == estrutura:
            return self.tipo
        elif self == estrutura1:
            return self.tipo1



estrutura = Molecula(formula=estrutura)
estrutura1 = Molecula(formula1=estrutura1)
print('A primeira molucela é um(a): ' + Molecula.informar_o_tipo(estrutura))
print('A primeira molucela é um(a): ' + Molecula.informar_o_tipo(estrutura1))
Molecula.reacao_quimica(estrutura)
