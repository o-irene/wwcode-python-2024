# Task: Write a function that counts the frequency of each word in a sentence.

def count_words(txt):
    txt_cleaned = ''.join(char for char in txt if char.isalpha() or char == ' ')
    words = txt_cleaned.split()
    words_count = {word: words.count(word) for word in set(words)}
    return words_count


if __name__ == "__main__":
    user_txt = input("Print the sentence for which you want to get a word count: ")
    user_words_count = count_words(user_txt)
    print(f'Here is the frequency of each word in your sentence: {user_words_count}')

