def is_all_vowels(str):
    vowels = "AEIOUaeiou"
    for ch in str:
        if ch not in vowels:
            return False
    return True
