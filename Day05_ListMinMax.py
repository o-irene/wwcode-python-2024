# Task: Write a program to find the maximum and minimum values in a list.

def find_extremums(ls):
    ls = [int(i) for i in ls]
    min_value = min(ls)
    max_value = max(ls)
    return min_value, max_value


def main():
    user_ls = input("Print the numbers, using space as a separator: ").split()
    try:
        min_ls, max_ls = find_extremums(user_ls)
        print(f"The minimum number in your list is {min_ls}, while the maximum is {max_ls}.")
    except ValueError:
        print("Only numbers are accepted. Try again and ensure you do not input any characters other than numbers.\n")
        main()


if __name__ == "__main__":
    main()
