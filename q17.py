# Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator. Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.

while True:
    try:
        num1 = int(input('Enter first number: '))
        break
    except ValueError:
        print('Invalid Number')


try:
    num2 = int(input('Enter second number: '))
except ValueError:
    print('Invalid Number')

operator = input('Enter operator: ')
validOperator = ['+', '-', '*', '**', '/', '//']
result = ''

if operator in validOperator:
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '**':
        result = num1 ** num2
    elif operator == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print('Error: Cannot divided by 0')
    else:
        try:
            result = num1 // num2
        except ZeroDivisionError:
            print('Error: Cannot divided by 0')
else:
    print('Invalid Operator!!!')

print(result)