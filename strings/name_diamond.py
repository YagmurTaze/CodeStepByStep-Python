def name_diamond(st):
    count = 0
    for i in range (len(st) *2):
        if count < len(st):
            print(st[:i])
            count += 1
        else:
            print(" " * (i - count) + st[(i - count):])