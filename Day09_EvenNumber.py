# Task: Write a program to check if a number is even or odd.
import random


def check_if_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    rand_int = random.randint(0, 100)
    if check_if_even(rand_int):
        print(f"{rand_int} is even.")
    else:
        print(f"{rand_int} is odd.")
