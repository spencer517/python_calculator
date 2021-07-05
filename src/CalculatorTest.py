import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_inst_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_calc_add(self):
        cal = Calculator()
        self.assertEqual(cal.add(3,2),5)

    def test_calc_subtract(self):
        cal = Calculator()
        self.assertEqual(cal.subtract(3,2),1)

    def test_calc_multiply(self):
        cal = Calculator()
        self.assertEqual(cal.multiply(3,2),6)

    def test_calc_divide(self):
        cal = Calculator()
        self.assertEqual(cal.divide(6,3),2)

if __name__ == '__main__':
    unittest.main()