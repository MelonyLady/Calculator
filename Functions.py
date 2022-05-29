#Calculator

#functions

def calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        return num1 / num2
    elif operator == '*':
        return num1 * num2


#variables

print('Please enter first number: ')
num1 = int(input())

print('Please choose your function: + - / *')


#making an exception rule

if True:
    try:
        operator = input()
        operator == "+" or "-" or "/" or "*"
    except:
           if operator != "+" or "-" or "/" or "*":
            print("The operator you have is invalid.")



print('Please enter second number')
num2 = int(input())



print("The answer is " + str(calc(num1, num2, operator)))



