# Task: Create a program that capitalizes the first letter of each word in a sentence

if __name__ == "__main__":
    user_txt = input("Print the sentence for which you want to get each word capitalized: ")
    if not user_txt:
        user_txt = 'You did not provide any text, so I generated this one for you.'
    user_txt_capitalized = user_txt.title()
    print(user_txt_capitalized)
