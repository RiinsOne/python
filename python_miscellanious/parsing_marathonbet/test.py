# import csv
#
# a = [[1.2,'abc',3], [1.2,'werew',4], [1.4,'qew',2]]
#
# with open("out.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(a)


x = [2, 3, 4, 5, 2, 2, 1, 3]
newx = []

for i in x:
    if i != 2:
        newx.append(i)

print(newx)

a = [1, 2, 3]
a.remove(2)
print(a)

