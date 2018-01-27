
#show fibonacci sequence up to Nth element
print("Show fibonacci sequence up to Nth element")
n = int(input("Enter number of elements..."))

n0 = 0 #first value of sequence is always equal to 0
n1 = 1 #second value of sequence is always equal to 1


def recursive_fib(n):
    if n <= 1:
        return n
    else:
        return (recursive_fib(n-1) + recursive_fib(n-2))


sequence = []

if n < 0:
    print("Please enter positive integer value")
elif n == 0:
    print("Fibonacci sequence n = 0 : ", n0)
else:
    print("Fibonacci sequence n = {0}".format(n))
    for i in range(n + 1):
        sequence.append(recursive_fib(i))

print(sequence)