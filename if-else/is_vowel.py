def is_vowel(str):
    vowels = 'AEIOUaeiou'
    if len(str) != 1:
        return False
    elif str in vowels:
        return True
    else:
        return False

#another option


def is_vowel(str):
            if str == "A" or str == "E" or str == "I" or str == "O" or str == "U" or str == "a" or str == "e" or str == "i" or str == "o" or str == "u":
                return True
            return False
