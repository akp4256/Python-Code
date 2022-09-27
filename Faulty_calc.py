num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operation you want to perform: ")

operation = operator.capitalize()

if operation == 'Addition':
    if num1 == 56 and num2 == 9:
        print("77")
    else:
        print(num1 + num2)
elif operation == 'Substraction':
    print(num1 - num2)
elif operation == 'Multiplication':
    if num1 == 45 and num2 == 3:
        print("555")
    else:
        print(num1 * num2)
elif operation == 'Division':
    if num1 == 56 and num2 == 6:
        print("4")
    else:
        print(num1 / num2)
else:
    print("Invalid Input!! Try Again.")
