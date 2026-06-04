
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a/b

n = int(input("Enter a number: "))
m = int(input("Enter another number: "))
option = input("Choose an operation (+, -, *, /): ")

if option == "+":
    result = add(n,m)
elif option == "-":
    result = subtract(n,m)
elif option == "*":
    result = multiply(n,m)
elif option == "/":
    result = divide(n,m)

print(f"The result of {n} + {m} is: {result}")