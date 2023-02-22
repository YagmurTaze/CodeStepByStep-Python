def xo(num):
    start = 0
    end = num - 1
    for i in range(num):
        for j in range (num):
            if j == start or j == end:
                print("x",end='')
            else:
                print("o",end='')
        start += 1
        end -= 1
        print()
