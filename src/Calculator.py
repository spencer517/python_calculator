class Calculator:
    result = 0

    def add(self,a,b):
        self.result = a + b
        return self.result

    def subtract(self,a,b):
        self.result = a - b
        return self.result

    def multiply(self,a,b):
        self.result = a * b
        return self.result

    def divide(self,a,b):
        a = float(a)
        b = float(b)
        self.result = a / b
        return self.result

    def __init__(self):
        pass