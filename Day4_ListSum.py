# Task: Write a program to find the sum of all elements in a list.

def sum_list_items(ls):
    ls = [int(i) for i in ls]
    ls_total_sum = sum(ls)
    return ls_total_sum


def main():
    user_ls = input("Print the numbers you want to sum up, using space as separator: ").split()
    try:
        sum_ls = sum_list_items(user_ls)
        print(f"The sum of your numbers is {sum_ls}.")
    except ValueError:
        print("Only numbers can be summed up. Try again and ensure you do not input items other than numbers.\n")
        main()


if __name__ == "__main__":
    main()
