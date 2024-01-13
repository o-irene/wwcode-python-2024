# Task: Write a function to count the number of vowels in a given string


def count_vowels(txt):
    vowels_ls = ['a', 'e', 'i', 'o', 'u']
    txt = txt.lower()
    vowels_num = sum([txt.count(letter) for letter in vowels_ls])
    return vowels_num


def main():
    user_txt = input("Please type some text: ")
    vowels_count = count_vowels(user_txt)
    print(f"The total number of vowels in your text is {vowels_count}.")


if __name__ == "__main__":
    main()
