# Task: Write a program to shuffle the elements of a list randomly.
import random


def shuffle_list(ls):
    random.shuffle(ls)
    return ls


if __name__ == "__main__":
    user_ls = input("Print the list items using space as a separator: ").split()
    print(f'Here is your list randomly shuffled: {shuffle_list(user_ls)}')
