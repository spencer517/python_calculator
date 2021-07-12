import unittest
import statistics
from Stats.StatisticsCalculator import StatisticsCalculator

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

    # def test_mode(self):
    #     nums = [1, 2, 3, 3, 3, 4, 5]
    #     self.assertEqual(self.stat_cal.mode(nums),3)

    def test_variance(self):
        nums = [1,3,7,9,11,24,30]
        var = statistics.variance(nums)
        var2 = self.stat_cal.variance(nums)
        self.assertEqual(round(var2,1),round(var,1))

    def test_std_dev(self):
        nums = [1, 3, 7, 9, 11, 24, 30]
        dev1 = statistics.stdev(nums)
        dev2 = self.stat_cal.stddev(nums)
        self.assertEqual(round(dev2, 2), round(dev1, 2))


if __name__ == '__main__':
    unittest.main()