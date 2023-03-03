def slash_figure():
    num = 22
    for i in range (6):
        print("\\\\" * i + "!" * num + "//" * i)
        num -= 4
