def addTwoNums(num1, num2):
    return num1 + num2

def subTwoNums(num1, num2):
    return num1 - num2

def divTwoNums(num1, num2):
    return num1 / num2

def mulTwoNums(num1, num2):
    return num1 * num2

print('Welcome to the Python calculator')

num1 = None 
num2 = None

while type(num1) != int:
    try:
        num1 = int(input('Please insert a number: '))
    except ValueError:
        print('You did not input a number')


while type(num2) != int:
    try:
        num2 = int(input('Please insert a second number: '))
    except ValueError:
        print('You did not input a number')

operator = input('What do you want to do? ')

if operator == 'add':
    print(addTwoNums(num1, num2))
elif operator == 'sub' or operator == 'subtract':
    print(subTwoNums(num1, num2))
elif operator == 'div' or operator == 'divide':
    print(divTwoNums(num1, num2))
elif operator == 'mul' or operator == 'multiply':
    print(mulTwoNums(num1, num2))
else:
    print('Bye')