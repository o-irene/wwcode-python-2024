# Task: Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def count_letters_case(txt):
    upper_case_count = 0
    lower_case_count = 0
    for letter in txt:
        if letter.isupper():
            upper_case_count += 1
        elif letter.islower():
            lower_case_count += 1
    return upper_case_count, lower_case_count


if __name__ == "__main__":
    user_txt = input("Print your text here: ")
    upper_letters, lower_letters = count_letters_case(user_txt)
    print(f"The text contains {upper_letters} upper letter and {lower_letters} lower letters.")
