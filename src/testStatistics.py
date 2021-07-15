import unittest
import statistics
from Stats.StatisticsCalculator import StatisticsCalculator
from Random.Rand import Rand

class StatisticsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.stat_cal = StatisticsCalculator()
        self.rand = Rand()

    def test_inst_stat_calculator(self):
        self.assertIsInstance(self.stat_cal, StatisticsCalculator)

    def test_mean(self):
        nums = self.rand.genRandIntListWithSeed(1, 10, 10)
        self.assertEqual(self.stat_cal.mean(nums),statistics.mean(nums))

    def test_median(self):
        nums = [1 , 2, 3]
        self.assertEqual(self.stat_cal.median(nums),2)

    def test_even_median(self):
        nums = [1 , 2, 3 , 4]
        self.assertEqual(self.stat_cal.median(nums),2.5)

    def test_mode(self):
        nums = self.rand.genRandIntListWithSeed(1, 20, 10)
        list = self.stat_cal.mode(nums)
        for i in list:
            mode = i
        self.assertEqual(mode,statistics.mode(nums))

    def test_variance(self):
        nums = self.rand.genRandIntListWithSeed(1, 50, 5)
        var = statistics.variance(nums)
        var2 = self.stat_cal.variance(nums)
        self.assertEqual(round(var2,0),round(var,0))

    def test_std_dev(self):
        nums = self.rand.genRandIntListWithSeed(1, 20, 10)
        dev1 = statistics.stdev(nums)
        dev2 = self.stat_cal.stddev(nums)
        self.assertEqual(round(dev2, 0), round(dev1, 0))


if __name__ == '__main__':
    unittest.main()