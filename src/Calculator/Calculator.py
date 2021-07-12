import math


class Calculator:
    result = 0

    def add(self,a,b):
        self.result = a + b
        return self.result

    def subtract(self,a,b):
        a = int(a)
        b = int(b)
        self.result = a - b
        return self.result

    def multiply(self,a,b):
        self.result = a * b
        return self.result

    def divide(self,a,b):
        a = float(a)
        b = float(b)
        self.result = a / b
        return round(self.result,6)

    def square(self,a):
        self.result = a * a
        return self.result

    def squareroot(self, a):
        a = float(a)
        self.result = math.sqrt(a)
        return round(self.result,3)

    def __init__(self):
        pass