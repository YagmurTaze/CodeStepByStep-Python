def start_end_letter(lt):
    print(f'Looking for two "{lt}" words in a row.')
    final_word = ""
    count = 0
    while count < 2:
        word = input("Type a word: ")
        if word[0].lower() == word[-1].lower() and word[0].lower() == lt:
            final_word = word
            count += 1 
        else:
            count = 0
    print(f'"{lt}" is for "{final_word}"')