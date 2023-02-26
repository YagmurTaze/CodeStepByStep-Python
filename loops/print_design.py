def print_design():
    num = 1
    for i in range (5):
        print("-" *  (5-i), end="")
        print(str(num) * num, end="")
        print("-" *  (5-i), end="")
        print()
        num += 2
