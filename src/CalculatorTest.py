import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_inst_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_calc_add(self):
        cal = Calculator()
        self.assertEqual(cal.add(3,2),5)

if __name__ == '__main__':
    unittest.main()