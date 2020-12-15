a = [2, 51, 'dd', -23, 105, 'ss', 8, 99, 'tt', 32]

halfLength = int(len(a) / 2)
fullLenght = int(len(a))

firstHalf = [a[i] for i in range(halfLength)]
secondHalf = [a[i] for i in range(halfLength, fullLenght)]

halfReverseList = secondHalf + firstHalf
print(halfReverseList)

# второй вариант
secondHalf.extend(firstHalf)
print(secondHalf)



#
