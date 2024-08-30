def reverse_word_order(s):
    if len(s) == 0:
        return ""
    arr = s.split()
    new_str = ""
    for i in range (len(arr) - 1):
        new_str += arr[len(arr) - 1 - i ] + " "
    new_str += arr[0]
    return new_str