def ascii_figure():
    for i in range (5):
        print("/" * (16 - (i * 4)), end="")
        print("*" * (i * 8), end="")
        print("\\" * (16 - (i * 4)), end="")
        print()
