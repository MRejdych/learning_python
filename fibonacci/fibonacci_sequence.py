#show fibonacci sequence up to Nth element
print("Show fibonacci sequence up to Nth element")
n = int(input("Enter number of elements..."))

n0 = 0 #first value of sequence is always equal to 0
n1 = 1 #second value of sequence is always equal to 1
count = 0

if n < 0:
    print("Please enter positive integer value")
elif n == 0:
    print("Fibonacci sequence n = 0 : ", n0)
else:
    print("Fibonacci sequence n = {0}".format(n))
    while count <= n:
        print(n0)
        # update variables
        nth = n0 + n1
        n0 = n1
        n1 = nth
        count += 1