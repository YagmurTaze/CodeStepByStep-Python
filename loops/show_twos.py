def show_twos(num):
    print(num,"=",end=" ")
    if num % 2 == 0:
        while num % 2 == 0:
            print("2 *",end=" ")
            num = num / 2
        print(int(num))
    else:
        print(num)
