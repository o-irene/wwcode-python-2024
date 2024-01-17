# Task: Write a program to check if a number is positive, negative, or zero.

def check_number_sign(number):
    if number > 0:
        sign = "positive"
    elif number == 0:
        sign = "zero"
    else:
        sign = "negative"
    print(f"Provided number is {sign}.")


def main():
    user_num = input("Print your number here: ")
    try:
        user_num = float(user_num)
        check_number_sign(user_num)
    except ValueError:
        print("Only numbers are accepted. Try again and ensure you do not input any characters other than numbers.\n")
        main()


if __name__ == "__main__":
    main()
