import unittest
from sisbanco import *

class TestConta(unittest.TestCase):
    
    def test_debitar(self):
        conta = Conta("123-X")
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), -5.0)

    def test_creditar(self):
        conta = Conta("123-X")
        conta.creditar(5)
        self.assertEqual(conta.get_saldo(), 0.0)

    def test_get_numero(self):
        conta = Conta("123-A")
        self.assertEqual(conta.get_numero(), "123-A")

    def test_get_saldo(self):
        conta = Conta("123-A")
        self.assertEqual(conta.get_saldo(), 0.0)
        
class TesteContaPoupanca(unittest.TestCase):

    def test_render_juros(self):
        conta = ContaPoupanca("122-C")
        conta.creditar(10)
        conta.render_juros(0.1)
        self.assertEqual(conta.get_saldo(), 11.0)

class TesteContaEspecial(unittest.TestCase):

    def test_render_bonus(self):
        conta = ContaEspecial("125-E")
        conta.creditar(10)
        self.assertEqual(conta.get_saldo(), 10)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 10.1)

class TesteContaImpost(unittest.TestCase):

    def test_taxa(self):
        conta = ContaImposto("121-D")
        self.assertEqual(conta.get_taxa(), 0.001)
        conta.set_taxa(0.1)
        self.assertEqual(conta.get_taxa(), 0.1)

    def test_debitar(self):
        conta = ContaImposto("121-D")
        conta.creditar(10)
        conta.debitar(1)
        self.assertEqual(conta.get_saldo(), 8.999)
        