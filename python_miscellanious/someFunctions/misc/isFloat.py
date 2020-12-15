from ogframework import newline

a = '3'
b = '4.0'
c = '5sd'

print(a.isdigit())
print(b.isdigit())
print(c.isdigit())


def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


newline()
print(isFloat(b))
print(isFloat(c))

#
