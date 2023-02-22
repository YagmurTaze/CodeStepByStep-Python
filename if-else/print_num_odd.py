def print_num_odd(n1, n2, n3):
    count = 0
    if n1 % 2 != 0:
        count += 1
    if n2 % 2 != 0:
        count += 1
    if n3 % 2 != 0:
        count += 1
    print(count, "of the 3 numbers are odd.")
