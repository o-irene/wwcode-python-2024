# Task: Write a program to reverse a given string.

def reverse_str(txt):
    return txt[::-1]


if __name__ == "__main__":
    user_txt = input("Print the text that you would like to get reversed: ")
    reversed_user_txt = reverse_str(user_txt)
    print(f"Here is your reversed text: \n{reversed_user_txt}")