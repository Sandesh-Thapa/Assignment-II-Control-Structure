# Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations, find the extension. For README.txt, the extension should be txt. Write code using slice operations that will give the name without the extension. Does your code work on filenames of arbitrary length?

filename = input('Enter filename with extension: ')
result = ''
for i in filename:
    if i != '.':
        result += i
    else:
        break

# Also works on filenames of arbitrary length

print(result)
