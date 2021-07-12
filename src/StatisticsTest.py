import unittest
from StatisticsCalculator import StatisticsCalculator

class StatisticsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.stat_cal = StatisticsCalculator()

    def test_inst_stat_calculator(self):
        self.assertIsInstance(self.stat_cal, StatisticsCalculator)

    def test_mean(self):
        nums = [1 , 2]
        self.assertEqual(self.stat_cal.mean(nums),1.5)

    def test_median(self):
        nums = [1 , 2, 3]
        self.assertEqual(self.stat_cal.median(nums),2)

    def test_even_median(self):
        nums = [1 , 2, 3 , 4]
        self.assertEqual(self.stat_cal.median(nums),2.5)


if __name__ == '__main__':
    unittest.main()