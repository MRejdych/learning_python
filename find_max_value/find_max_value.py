numbers = [5, 10, 11, 1, 2, 20, 3, 3, 9, 7, 51]

maxVal = 0

for number in numbers:
    if number > maxVal:
        maxVal = number

print("Max value from given list: {}".format(maxVal))
