# Program to check if a number is divisible by another

# Take user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check divisibility
if num2 != 0:   # avoid division by zero
    if num1 % num2 == 0:
        print(num1, "is divisible by", num2)
    else:
        print(num1, "is NOT divisible by", num2)
else:
    print("Division by zero is not allowed.")
