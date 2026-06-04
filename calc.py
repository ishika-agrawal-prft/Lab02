
def add(a,b):
    return a+b


n = int(input("Enter a number: "))
m = int(input("Enter another number: "))
option = input("Choose an operation (+, -, *, /): ")

if option == "+":
    result = add(n,m)

print(f"The result of {n} + {m} is: {result}")