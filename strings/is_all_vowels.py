def is_all_vowels(str):
    vowels=['A','E','I','O','U','a','e','i','o','u']
    for i in range (len(str)):
        if not str[i] in vowels:
            return False
    return True