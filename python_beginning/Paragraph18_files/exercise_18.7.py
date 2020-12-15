def stringCount(fileName, stringName):
    count = 0
    with open(fileName) as textFile:
        for i in textFile:
            i = i.strip()
            if stringName == i:
                count += 1
    return count


print(stringCount('18_7.txt', 'total_handicap'))

#
