# calculator.py

def add(x, y):
    z = x + y;
    print("{} + {} = {}".format(x, y, z))
    return z

x = input("Input a letter: ")
print("You entered {}.".format(x))
print("Here is a line of code.")

if x == "a":
    z = add(100, 2)
    if z > 100:
        print("This number is too high.")

elif x == "s":
    a = 1;
    b = 2;
    c = a - b;
    print("{} - {} = {}".format(a, b, c))
else:
    print("The \"{}\" command is not recognized.".format(x))
print("Done.")
