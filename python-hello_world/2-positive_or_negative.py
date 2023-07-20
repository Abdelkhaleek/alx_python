#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Check if the number is positive or negative
if number > 0:
    print("The number {} is positive".format(number))
elif number < 0:
    print("The number {} is negative".format(number))
else:
    print("The number is 0")
