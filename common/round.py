class circle:
    def __init__(self, starterValue, maxValue, minValue):
        self.minValue = minValue
        self.maxValue = maxValue
        self.range = (maxValue - minValue) + 1
        self.value = starterValue
        self.wrapcounter = 0


    def increase(self, amount):
        raw = self.value + amount
        self.wrapcounter += abs((raw - self.minValue) // self.range)
        self.value = ((raw - self.minValue) % self.range) + self.minValue


    def decrease(self, amount):
        raw = self.value - amount
        self.wrapcounter += abs((raw - self.minValue) // self.range)
        self.value = ((raw - self.minValue) % self.range) + self.minValue

