from random import randint

# надо доделать

lst = [randint(1, 10) for i in range(1, 21)]
print('list', lst)
print(len(lst))

fstIndex = 0
scndIndex = 1

count = 0

newLst = list()

for i in lst:
    if scndIndex > len(lst) - 1:
        break
    elif lst[scndIndex] > lst[fstIndex]:
        newLst.append(1)
    else:
        newLst.append(0)

    fstIndex += 1
    scndIndex += 1

# newStr = str.join('', newLst)

print(newLst)

fstIndex = 0
scndIndex = 1

for i in newLst:
    if sum(newLst[fstIndex:scndIndex+1]) == 1:
        count += 1
    fstIndex += 1
    scndIndex += 1

result = 0
print(count)

if count % 2 == 0:
    result += count / 2
else:
    result += (count + 1) / 2

print(result)


#
