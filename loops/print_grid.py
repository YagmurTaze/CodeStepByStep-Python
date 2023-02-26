def print_grid(row, col):
    for i in range (1, row+1):
        print(i,end="")
        num = 0
        for j in range (1, col):
            print(",",i + row + num,end="")
            num += row
        print()
