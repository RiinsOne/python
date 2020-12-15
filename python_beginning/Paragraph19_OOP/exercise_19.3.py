class StringVar:
    string = ''

    def __init__(self, strVal):
        self.string = strVal

    def setVal(self, strVal):
        self.string = strVal

    def getVal(self):
        return self.string


newStr = StringVar('total_handicap')
print(newStr)  # <__main__.StringVar object at 0x00B03410>
print(newStr.getVal())  # total_handicap
newStr.setVal('OG')
print(newStr.getVal())  # OG







#
