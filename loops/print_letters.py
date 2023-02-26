def print_letters(text):
    if len(text) == 0:
        return
    print(text[0],end="")
    for i in range(1, len(text)): 
        print("-" + text[i], end="")
    print()   
