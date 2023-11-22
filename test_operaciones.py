import unittest
from operaciones import sumar, restar, multiplicar, dividir

class TestOperaciones (unittest.TestCase):
    def test_sumar(self):
        self. assertEqual(sumar (5, 2), 7)
        self. assertEqual (sumar (-1, -2), -3)
        self. assertEqual (sumar (3, 2), 5)
    def test_restar(self):
        self. assertEqual(restar (4, 2), 2)
        self. assertEqual(restar(5, 1), 4)
        self. assertEqual (restar(4, 1), 3)
    def test_multiplicar(self):
        self. assertEqual(multiplicar (2, 2), 4)
        self. assertEqual(multiplicar(3, 2), 6)
        self. assertEqual(multiplicar(1, 1), 1)
    def test_dividir(self):
        self. assertEqual (dividir(9, 3), 3)
        self. assertEqual (dividir(4, 2), 2)
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()
