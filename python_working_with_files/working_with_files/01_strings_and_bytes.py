import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


print(ord('h'))  # code 104
print(chr(104))  # symbol h

for ch in 'hello':
    print(ord(ch))

print('-----')

codes = [104, 101, 108, 108, 111, ]
out = ''
for code in codes:
    out += chr(code)
print(out)

print('-----')

# for code in range(128):
#     print(code, hex(code), chr(code))
# таблица символов ASCII

# unicode - содержит все символы

# for code in range(1000, 1200):
#     print(code, chr(code))
# utf-8

bb = b'\xd1\x85'
print(bb)

print('-----')

bb = b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
print(bb)
print(type(bb))
# по сути это неизменяемые последовательности целых чисел,
# поддерживают те же операции что и str
print(bb[0])
print(hex(bb[0]))
print(bb.count(0xd0))
print(b'he' + b'llo')

print('-----')

bb = b'\xd1\x85'
print(bin(0xd1))
print(bin(0x84))

code = 0b10001000100
print(code, hex(code))  # 1092 0x444
print(chr(code))  # ф
