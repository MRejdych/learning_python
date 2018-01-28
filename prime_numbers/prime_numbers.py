# prints all prime numbers in given interval

start = int(input("Enter start value..."))
end = int(input("Enter end value..."))

print("All prime numbers between {0} and {1}: ".format(start, end))

prime_numbers = []

for number in range(start, end + 1):
    if number <= 1:
        continue
    for i in range(2, number):
        if (number % i) == 0:
            break
    else:
        prime_numbers.append(number)

print(prime_numbers)