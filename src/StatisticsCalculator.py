from Calculator import Calculator

class StatisticsCalculator(Calculator):
    result = 0
    numlist = []

    def mean(self, numbers):
        try:
            length = len(numbers)
            summedNums = sum(numbers)
            self.result = Calculator.divide(self, summedNums, length)
            return  round(self.result,2)
        except ZeroDivisionError:
            print("Error: Please use a list that contains at least 1 number")

    def median(self, numbers):
        try:
            length = len(numbers)
            self.numlist = numbers
            if length % 2 == 0:
                num1 = self.numlist[int(length/2)]
                num2 = self.numlist[int(Calculator.subtract(self,(length/2),1))]
                self.result = Calculator.divide(self,Calculator.add(self, num1, num2), 2)
                return self.result
            else:
                self.result = self.numlist[int(Calculator.divide(self, length ,2))]
                return self.result
        except ZeroDivisionError:
            print("Error: Please use a list that contains at least 1 number")

    def mode(self):
        pass

    def stddev(self):
        pass

    def variance(self):
        pass

    def __init__(self):
        pass