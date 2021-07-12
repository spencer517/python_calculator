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

    def mode(self, numbers):
        try:
            length = len(numbers)
            self.numlist = numbers
            count = 0

            return 2
        except:
            Exception
            print("error")


    def stddev(self,numbers):
        var = self.variance(numbers)
        self.result = Calculator.squareroot(self, var)
        return self.result

    def variance(self, numbers):
        length = len(numbers)
        varmean = self.mean(numbers)
        var = 0
        try:
            for i in numbers:
                var += Calculator.square(self, Calculator.subtract(self,i, varmean))
            self.result = Calculator.divide(self, var, length-1)
            return self.result
        except ZeroDivisionError:
            print("Error can't divide by zero")
        pass

    def __init__(self):
        pass