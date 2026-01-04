# Write a program using match case that stimulates a simple calculator
# 1. Ask the user for two numbers and operations (+,-,/,*)
# 2. Perform the operation using match case

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose operation: ")

match operation:
    case "+":
        print(num1, "+", num2, "=", (num1+num2))
    case "-":
        print(num1, "-", num2, "=", (num1-num2))
    case "*":
        print(num1, "*", num2, "=", (num1*num2))
    case "/":
        print(num1, "/", num2, "=", (num1/num2))
        