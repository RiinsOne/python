import re

print(re.search('r[ea]d', 'rad'))  # <re.Match object; span=(0, 3), match='rad'>
print(re.search('r[ea]d', 'read'))  # None

print(re.search('[1-8]', '3'))  # <re.Match object; span=(0, 1), match='3'>
print(re.search('[1-8]', '9'))  # None

#
