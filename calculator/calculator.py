
# Adds two numbers
def add(x, y):
    return x + y

# Substracts two numbers
def sub(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Divides number x by y
def division(x, y):
    return x / y

# x to y power
def power(x, y):
    return x**y

print("Select operation:")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

choice = input("Enter choice ...")

x = int(input("Enter first value..."))
y = int(input("Enter second value..."))

if choice == '1':
    print("{0}+{1} = {2}".format(x, y, add(x, y)))
elif choice == '2':
    print("{0}-{1} = {2}".format(x, y, sub(x, y)))
elif choice == '3':
    print("{0}*{1} = {2}".format(x, y, multiply(x, y)))
elif choice == '4':
    print("{0}/{1} = {2}".format(x, y, division(x, y)))
elif choice == '5':
    print("{0}^{1} = {2}".format(x, y, power(x, y)))
else:
    print("Invalid input!")