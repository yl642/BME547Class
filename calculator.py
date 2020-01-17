# calculator.py

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y;
    return z

def divide(x, y):
    z = x / y;
    return z

x = input("Enter an operation type you want to make (+-*/): ")
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

if x == "+":
    z = add(a, b)
    print("{} {} {} = {}".format(a, x, b, z))
elif x == "-":
    z = subtract(a, b)
    print("{} {} {} = {}".format(a, x, b, z))
elif x == "*":
    z = multiply(a, b)
    print("{} {} {} = {}".format(a, x, b, z))
elif x == "/":
    z = divide(a, b)
    print("{} {} {} = {}".format(a, x, b, z))
else:
    print("The \"{}\" command is not recognized.".format(x))
print("Done.")
