class UppercaseException(Exception):
    pass


words = ['q', 'r', 'm', 'M']
for word in words:
    if word.isupper():
        raise UppercaseException(word)

# Traceback (most recent call last):
#   File "M:/Programs/workspace/programming/python/python_beginning/Paragraph19_OOP/ownException.py", line 8, in <module>
#     raise UppercaseException(word)
# __main__.UppercaseException: M




















#
