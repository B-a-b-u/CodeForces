n = int(input()) # No of words
for _ in range(n):
    word = input().strip()  # Getting new word
    len_of_word = len(word)
    if len_of_word > 10:
        # abbrevation =f"{word[0]}{len_of_word-2}{word[-1]}" # method 1
        abbrevation = word[0] + str(len_of_word-2) + word[-1]
        print(abbrevation)
    else:
        print(word)