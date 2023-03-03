def slash_figure2():
    num = SIZE * 4 - 2
    for i in range (SIZE):
        print("\\\\" * i + "!" * num + "//" * i)
        num -= 4
