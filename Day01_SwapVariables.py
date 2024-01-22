# Task: Create a program that swaps the values of two variables.
import random

var1 = random.randint(0, 100)
var2 = random.randint(0, 100)


def swap_values():
    global var1, var2
    var1, var2 = var2, var1


print(f'Values before swap: {var1}, {var2}.')
swap_values()
print(f'Values after swap: {var1}, {var2}.')