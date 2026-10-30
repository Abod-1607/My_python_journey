oper = input("Choose your operation (add, subtract, multiply, divide, modulus): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if oper == "add":
    result = num1 + num2
    print("The sum is:", result)
elif oper == "subtract":
    result = num1 - num2
    print("The subtraction is:", result)
elif oper == "multiply":
    result = num1 * num2
    print("The multiplication is:", result)
elif oper == "divide":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("The division is:", result)
elif oper == "modulus":
    if num2 == 0:
        print("Error: Modulus by zero is not allowed.")
    else:
        result = num1 % num2
        print("The modulus is:", result)
else:
    print("Invalid operation")


