print("Select operation:")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

add = lambda a, b: a + b
sub = lambda a, b: a - b
multiply = lambda a, b: a*b
divide = lambda a, b: a/b
power = lambda a, b: a**b


def switch(val):
    return {
        1: add,
        2: sub,
        3: multiply,
        4: divide,
        5: power
    }.get(val, lambda a, b: print("Invalid input! {0}, {1}".format(a, b)))


choice = int(input("Enter choice ..."))

x = int(input("Enter first value..."))
y = int(input("Enter second value..."))

print(switch(choice)(x, y))
