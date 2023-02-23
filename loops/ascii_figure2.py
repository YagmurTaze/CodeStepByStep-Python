def ascii_figure2():
    for i in range (HEIGHT):
        print("/" * (((HEIGHT-1)*4) - (i * 4)), end="")
        print("*" * (i * 8), end="")
        print("\\" * (((HEIGHT-1)*4) - (i * 4)), end="")
        print()
