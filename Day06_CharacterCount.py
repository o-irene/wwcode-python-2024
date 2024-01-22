# Task: Write a program to count the occurrences of a specific character in a string.

def count_character(txt, char):
    txt = txt.lower()
    char = char.lower().strip()
    total_count = txt.count(char)
    return total_count


if __name__ == "__main__":
    user_txt = input("Print your text here: ")
    char_to_count = input("Which character do you want to count in it? ")
    char_count = count_character(user_txt, char_to_count)
    print(f"Here is how many times '{char_to_count}' is repeated in your text: {char_count}.")
