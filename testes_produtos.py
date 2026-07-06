import unittest
from funcoes.func_crud import validar_senha_adm

class TesteSenhaAdministrador(unittest.TestCase):

    def test_senha_correta(self):
        self.assertTrue(validar_senha_adm(123))

    def test_senha_errada(self):
        self.assertFalse(validar_senha_adm(111))

if __name__ == "__main__":
    unittest.main()