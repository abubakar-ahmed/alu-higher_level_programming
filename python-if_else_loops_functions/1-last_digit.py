#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digits = abs(number) % 10
if number < 0:
    digit = -digit
Print("Last digit of {} is {} and is ".format(number, digit),
 end="")
if digit > 5:
    Print("greater than 5")
elif digit == 0:
    Print("0")
else:
    Print("less than 6 and not 0")
