#!/usr/bin/python3
import random
number = ramdom.randint(-10000, 10000)
digits = abs(number) % 10
if number < 0:
    digit = -digit
print("Last digit of {} is {} and is ".format(number, digit),
 end="")
if digit is > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
