import subprocess as sp

# write directyle to file
# with open('output.txt', 'w') as f:
#     p1 = sp.run(['ls', '-la'], stdout=f)

# p2 = sp.run(['ls', '-la', 'dne'], stdout=sp.PIPE, stderr=sp.DEVNULL)
# print(p2.stderr)

p3 = sp.run(['cat', 'test.txt'], stdout=sp.PIPE)
print(p3.stdout.decode())
p5 = p3.stdout.decode()
print(p5)

p4 = sp.run(['grep', '-n', 'test'], stdout=sp.PIPE, input=p5)

print()
