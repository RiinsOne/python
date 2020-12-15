L = [3, 6, 7, 4, -5, 4, 3, -1]

if sum(L) > 2:
    print(len(L))

diff = min(L) - max(L)
print(abs(diff))
if abs(diff) > 10:
    print(sorted(L))
else:
    print(f'The difference between the numbers is {diff}')

#
