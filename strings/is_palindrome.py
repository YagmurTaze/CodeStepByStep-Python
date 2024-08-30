def is_palindrome(s):
    s = s.lower()
    for i in range(0, len(s)//2):
        if not s[i] == s[( len(s) - 1 - i)]:
            return False
    return True