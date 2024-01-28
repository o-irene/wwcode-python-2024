# Task: Create a program that capitalizes the first letter of each word in a sentence

if __name__ == "__main__":
    user_txt = input("Print the sentence for which you want to get each word capitalized: ")
    user_txt_capitalized = user_txt.title()
    print(user_txt_capitalized)
