def print_num_range(int1, int2):
    print("[",end="")
    if int1 < int2:
        for i in range(int1, int2+1):
            print(str(i),end="")
            if i < int2:
                print(", ",end="")
    elif int2 < int1:
        for i in range(int1, int2-1, -1):
            print(str(i),end="")
            if i > int2:
                print(", ",end="")
    else:
        print(str(int1),end="")
    print("]")
