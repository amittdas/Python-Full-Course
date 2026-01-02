# Write a program that asks the user for a number and prints whether it is positive, negative and zero.

num = int(input("Enter the Number: "))

if(num<0):
    print("The number is negative")
elif(num == 0):
    print("The number is Zero")
else:
    print("The number is positive")