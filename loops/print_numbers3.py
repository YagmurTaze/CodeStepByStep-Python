def print_numbers3():
    for i in range(1,6):
        print("." * (5 - i),end="")
        print(i,end="")
        print("." * (i-1))
