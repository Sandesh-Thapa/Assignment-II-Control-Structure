# Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e. this_is_camel_cased). Modify the function by adding an argument, separator, so it will also convert to the kebab case (i.e.this-is-camel-case) as well.

def convertStringCase(camel, separator):
    output = ''
    if separator == None:
        if camel[0].isupper():
            output += camel[0].lower()
            for i in range(1, len(camel)):
                if camel[i].isupper():
                    output += f'_{camel[i].lower()}'
                else:
                    output += camel[i]
            print(output)
        else:
            print('Enter string in camel-cased format !!')
    elif separator == '-':
        if camel[0].isupper():
            output += camel[0].lower()
            for i in range(1, len(camel)):
                if camel[i].isupper():
                    output += f'{separator}{camel[i].lower()}'
                else:
                    output += camel[i]
            print(output)
        else:
            print('Enter string in camel-case format !!')

    
        
string = input("Enter string in camel-case format: ")

convertStringCase(string, None)
convertStringCase(string, '-')