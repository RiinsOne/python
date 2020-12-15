from ogframework import newline

s = "У лукоморья 123 дуб зеленый 456"

# 1
if s.count('я'):
    print(s.find('я'))

# 2
newline()
print(s.count('у'))

# 3
newline()
if not s.isalpha():
    print(s.upper())
    print(str.upper(s))

# 4
newline()
if len(s) > 4:
    print(f'len of str = {len(s)}')
    print(s.lower())

# 5
newline()
new_str = 'O' + s[1:]
print(new_str)

#
