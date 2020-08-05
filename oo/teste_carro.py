from unittest import TestCase

from oo.carroPB import Motor


class CarroTestCase(TestCase):
    def teste_velociddade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

