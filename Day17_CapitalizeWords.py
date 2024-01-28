# Task: Create a program that capitalizes the first letter of each word in a sentence

def capitalize_words(txt):
    words_ls = txt.split()
    words_capitalized = [word.title() for word in words_ls]
    return ' '.join(words_capitalized)


if __name__ == "__main__":
    user_txt = input("Print the sentence for which you want to get each word capitalized: ")
    user_txt_capitalized = capitalize_words(user_txt)
    print(user_txt_capitalized)
