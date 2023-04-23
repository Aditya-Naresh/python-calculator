def calculate(num1, num2):
    operation = input("Enter the operation")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '*':
        result = num1 * num2
    else:
        print("Invalid operation")
        return

    print(result)


num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

calculate(num1, num2)
