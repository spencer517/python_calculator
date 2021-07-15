from Calculator.Calculator import Calculator
from collections import Counter

class StatisticsCalculator(Calculator):
    result = 0
    numlist = []

    def mean(self, numbers):
        try:
            length = len(numbers)
            summedNums = sum(numbers)
            self.result = Calculator.divide(self, summedNums, length)
            return  self.result
        except ZeroDivisionError:
            print("Error: Please use a list that contains at least 1 number")
        except TypeError:
            print("Please enter only numbers.")

    def median(self, numbers):
        try:
            length = len(numbers)
            self.numlist = numbers
            if len == 0:
                return print("Please enter a list containing at least 1 number")
            elif length % 2 == 0:
                num1 = self.numlist[int(length//2)]
                num2 = self.numlist[int(Calculator.subtract(self,(length//2),1))]
                self.result = Calculator.divide(self,Calculator.add(self, num1, num2), 2)
                return self.result
            else:
                self.result = self.numlist[int(Calculator.divide(self, length ,2))]
                return self.result
        except ZeroDivisionError:
            print("Error: Please use a list that contains at least 1 number")
        except TypeError:
            print("Please enter only numbers.")

    def mode(self, numbers):
        try:
            count = Counter(numbers)
            self.result=[i for i, obs in count.items() if obs == count.most_common(1)[0][1]]
            return self.result
        except ZeroDivisionError:
            print("Error: Please use a list that contains at least 1 number")
        except TypeError:
            print("Please enter only numbers.")


    def stddev(self,numbers):
        if len(numbers) == 0:
            print("Error: Please use a list that contains at least 1 number")
        else:
            try:
                var = self.variance(numbers)
                self.result = Calculator.squareroot(self, var)
                return self.result
            except ZeroDivisionError:
                print("Error can't divide by zero")
            except TypeError:
                print("Please enter only numbers.")

    def variance(self, numbers):
        length = len(numbers)
        varmean = self.mean(numbers)
        var = 0
        if length == 0:
            print("Error: Please use a list that contains at least 1 number")
        else:
            try:
                for i in numbers:
                    var += Calculator.square(self, Calculator.subtract(self,i, varmean))
                self.result = Calculator.divide(self, var, length-1)
                return self.result
            except ZeroDivisionError:
                print("Error can't divide by zero")
            except TypeError:
                print("Please enter only number.")

    def __init__(self):
        pass