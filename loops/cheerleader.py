def cheerleader(line, cheer):
    for i in range (line):
        str ="Go "
        str2 ="Team "
        print()
        print(" " * (i*3),end="")
        for j in range (cheer-1):
            print(str,end="")
            print(str2,end="")
        print(str,end="")
