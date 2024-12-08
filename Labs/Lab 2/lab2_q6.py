num1 = float(input("Enter your first number: "))
operation = input("Enter the operation (+, -, *, / ): ")
num2 = float(input("Enter your second number: "))

if operation == "+":
    result = num1 + num2
    print(num1, operation, num2, "=", result)
elif operation == "-":
    result = num1 - num2
    print(num1, operation, num2, "=", result)
elif operation == "*":
    result = num1 * num2
    print(num1, operation, num2, "=", result)

elif operation == "/":
    result = num1 / num2
    print(num1, operation, num2, "=", result)
else:
    print(num1, operation, num2, "is an invalid operation.")