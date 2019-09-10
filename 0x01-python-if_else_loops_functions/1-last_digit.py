#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d}" .format(number), end=" ")
if number > 0:
    LastDig = number % 10
else:
    LastDig = number % -10
if LastDig > 5:
    print("is {:d} and is greater than 5" .format(LastDig))
elif LastDig < 6 and LastDig != 0:
    print("is {:d} and is less than 6 and not 0" .format(LastDig))
else:
    print("is {:d} and is 0" .format(LastDig))
