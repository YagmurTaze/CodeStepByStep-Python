def print_palindrome ():
    words = input("Type one or more words: ")
    result = is_palindrome(words)
    if result:
        print(words + " is a palindrome!")
    else:
        print(words + " is not a palindrome.")
        
def is_palindrome(s):
    s = s.lower()
    for i in range(0, len(s)//2):
        if not s[i] == s[( len(s) - 1 - i)]:
            return False
    return True