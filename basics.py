# basics
x = input("Input a letter: ")
print("You entered {}.".format(x))
print("Here is a line of code.")
if x == "a":
    a = 1;
    b = 2;
    c = a + b;
    print("{} + {} = {}".format(a, b, c))
elif x == "s":
    a = 1;
    b = 2;
    c = a - b;
    print("{} - {} = {}".format(a, b, c))
else:
    print("The \"{}\" command is not recognized.".format(x))
print("Done.")
