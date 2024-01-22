# Task: Write a program to print the multiplication table of a given number.

def get_multiplication_table(num):
    for i in range(1, 11):
        product = num * i
        print(f'{num} * {i} = {product}')


def main():
    user_num = input("Print the number for which you want to get a multiplication table: ")
    try:
        user_num = int(user_num)
        get_multiplication_table(user_num)
    except ValueError:
        print("Only numbers are accepted. Try again and ensure you do not input any characters other than numbers.\n")
        main()


if __name__ == "__main__":
    main()
