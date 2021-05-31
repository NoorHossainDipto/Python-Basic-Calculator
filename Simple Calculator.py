num1 = int(input('number 1: '))
num2 = int(input('number 2: '))
sum = input('sum : ')

if sum == "+":
    print(num1 + num2)
elif sum == "-":
    print(num1 - num2)
elif sum == "/":
    print(num1 / num2)
elif sum == "*":
    print(num1 * num2)
else :
    print("Invalid Syntax")
    
