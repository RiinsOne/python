with open('file_examples\\plan.txt') as file:
    contents = file.readlines()
    contents.sort()
print(contents)

with open('file_examples\\sort_plan.txt', 'w') as output_file:
    for line in contents:
        output_file.write(line.strip() + ' ')
        # output_file.write(' ')
        # output_file.write(line)

#
