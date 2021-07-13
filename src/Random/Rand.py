import random


class Rand:

    def __init__(self):
        pass

    def genRandIntWithoutSeed(self, num1, num2):
        x = random.randrange(num1, num2)
        return x

    def genRandIntWithSeed(self, num1, num2):
        random.seed()
        x = random.randrange(num1, num2)
        return x

    def genFloatIntWithoutSeed(self, num1, num2):
        x = random.uniform(num1, num2)
        return x

    def genFloatIntWithSeed(self, num1, num2):
        random.seed()
        x = random.uniform(num1, num2)
        return x


    def genRandIntListWithSeed(self, num1, num2, listSize):
        randList = []
        random.seed()
        i =0
        while i < listSize:
            x = random.randrange(num1, num2)
            randList.append(x)
            i+=1
        return randList

    def genFloatIntListWithSeed(self, num1, num2, listSize):
        randList = []
        random.seed()
        i =0
        while i < listSize:
            randNum = random.uniform(num1, num2)
            randList.append(randNum)
            i+=1
        return randNum
