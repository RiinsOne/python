import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# print(r'\tTab')  # \tTab

pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)  # <re.Match object; span=(1, 4), match='abc'>

print(text_to_search[1:4])  # abc

print('------')

pattern_two = re.compile(r'end$')

matches_two = pattern_two.finditer(sentence)
for match in matches_two:
    print(match)

print('------')

pattern_three = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern_three = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# [1-5] - все цифры от 1 до 5
# [a-z] - все буквы от a до z

matches_three = pattern_three.finditer(text_to_search)
for match in matches_three:
    print(match)

print('------')

# pattern_four = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches_four = pattern_four.finditer(contents)
#     for match in matches_four:
#         print(match)

print('------')

pattern_4 = re.compile(r'\d{3}.\d{3}.\d{4}')
matches_4 = pattern_4.finditer(text_to_search)
for match in matches_4:
    print(match)

print('------')

pattern_5 = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches_5 = pattern_5.finditer(text_to_search)
for match in matches_5:
    print(match)

print('------')

pattern_6 = re.compile(r'\d{3}.\d{3}.\d{4}')
# matches_6 = pattern_6.findall(text_to_search)
# or
matches_6 = re.findall(pattern_6, text_to_search)
for match in matches_6:
    print(match)
# если есть группа, то вернет первую группу, если несколько групп, то кортеж из групп
print(type(matches_6))  # class list

print('------')

# pattern_7 = re.compile(r'Start')
# pattern_7 = re.compile(r'start', re.IGNORECASE)  # искать в любом регистре
pattern_7 = re.compile(r'start', re.I)  # искать в любом регистре
matches_7 = pattern_7.match(sentence)
# matches_7 = pattern_7.search(sentence)
print(matches_7)
# match - только начало строки
# search - ищет везде
