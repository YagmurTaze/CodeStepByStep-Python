def flip_coin_three_heads():
    h_count = 0
    while h_count != 3:
        flip = random.randint(0,1)
        if flip == 0:
            print("H",end=" ")
            h_count += 1
        else:
            print("T",end=" ")
            h_count = 0
    print()
    print("Three heads in a row!")
