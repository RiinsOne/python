def compare(string, number):
    if len(string) > number:
        return str.upper(string)
    else:
        return str.lower(string)


print(compare('total_handicap', 3))
print(compare('tESt', 4))


#
