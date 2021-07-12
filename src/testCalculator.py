import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_inst_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_csv_add(self):
        reader = CsvReader('/src/Addition.csv').data
        for row in reader:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_csv_subtract(self):
        reader = CsvReader('/src/Subtraction.csv').data
        for row in reader:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_csv_multiply(self):
        reader = CsvReader('/src/Multiplication.csv').data
        for row in reader:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_csv_divide(self):
        reader = CsvReader('/src/Division.csv').data
        for row in reader:
            self.assertEqual(self.calculator.divide(float(row['Value 1']), float(row['Value 2'])), round(float(row['Result']),6))

    def test_csv_square(self):
        reader = CsvReader('/src/Square.csv').data
        for row in reader:
            self.assertEqual(self.calculator.square(int(row['Value 1'])),  int(row['Result']))

    def test_csv_squareroot(self):
        reader = CsvReader('/src/SquareRoot.csv').data
        for row in reader:
            self.assertEqual(self.calculator.squareroot(int(row['Value 1'])),  round(float(row['Result']),3))

if __name__ == '__main__':
    unittest.main()