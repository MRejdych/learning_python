try:
    2 + 'string'
except TypeError:
    print("TypeError catched, you can not add string to integer")
else:
    print("This block will be run, when there was no exception")
finally:
    print("This block will be run even if exception was thrown, just like in Java")

try:
    2 + 1
except TypeError:
    print("This time TypeError will not be raised.")
else:
    print("This block will be run, when there was no exception")
finally:
    print("This block will be run even if exception was thrown, just like in Java")

try:
    raise TypeError("Demonstrating how to raise exception")
except TypeError as ex:
    print(ex)
    print("TypeError catched")
finally:
    print("This block will be run even if exception was thrown, just like in Java")

try:
    raise TypeError("Demonstrating how to raise exception")
except TypeError:
    print("More specific error will be catched")
except Exception:
    print("...")

try:
    raise Exception("...")
except TypeError:
    print("Less specific error will not be catched")
except Exception as e:
    print(e)
