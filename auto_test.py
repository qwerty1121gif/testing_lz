from auto_test_func import heand
import unittest

class Test_func(unittest.TestCase):
    def test_pos(self):
        self.assertEqual(heand(123), 1.5711511089688401)

    def test_neg(self):
        self.assertEqual(heand(-123), "Ошибка вычисления логарифма из отрицательного числа или нуля\единицы")

    def test_one(self):
        self.assertEqual(heand(1), "Ошибка вычисления логарифма из отрицательного числа или нуля\единицы")

    def test_zero(self):
        self.assertEqual(heand(0), "Ошибка вычисления логарифма из отрицательного числа или нуля\единицы")

    def test_str(self):
        self.assertEqual(heand('a'), "Ошибка типов данных")

    def test_zero_input(self):
        self.assertEqual(heand(''), "Ошибка типов данных")

    def test_float(self):
        self.assertEqual(heand(1.1), -2.3506186555132937)

if __name__ == "__main__":
    unittest.main()