#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Check if the number is positive or negative
if number > 0:
    print("{} is positive".format(number))
elif number < 0:
    print("{} is negative".format(number))
else:
    print("is zero")
