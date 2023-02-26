def print_pyramid():
    num = 0
    for i in range(1, 7):
        print(" " * (7-i),end="")
        print("*" * (i + num))
        num += 1
# or

def print_pyramid():
    for i in range(1, 7):
        for j in range(0, 7 - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            print("*", end="")
        print("")
