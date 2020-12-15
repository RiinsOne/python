class Point:
    x, y = 0, 0

    def __init__(self, xVal, yVal):
        self.x, self.y = xVal, yVal

    def setNewPair(self, xVal, yVal):
        self.x, self.y = xVal, yVal

    def setNewX(self, xVal):
        self.x = xVal

    def setNewY(self, yVal):
        self.y = yVal

    def getVal(self):
        return self.x, self.y

    def getValX(self):
        return self.x

    def getValY(self):
        return self.y


pair: Point = Point(5, 4)
print(pair.getVal())  # (5, 4)
print(pair.getValX())  # 5
print(pair.getValY())  # 4

pair.setNewPair(87, 44)
print(pair.getVal())  # (87, 44)
pair.setNewY(841)
print(pair.getVal())  # (87, 841)





#
