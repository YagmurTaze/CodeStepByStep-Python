def plus_line():
    print("+------------------------------+",end="")

def py():
    print("|    How to Code in Python     |",end="")

def space(num):
    print(" " * num,end="")
    
def slash(num):
    print("/" * num)
     
def us_slash_3():
    print("___/",end="")

def us_slash_2(num):
    print("__/" * num ,end="")
    
def main():
    num = 0
    print("           ",end="")
    plus_line()
    print()
    for i in range (1,11):
        space(11 - i)
        print("/",end="")
        space(27 - num)
        num += 3
        us_slash_3()
        us_slash_2(i-1)
        slash(i-1)
    plus_line()
    slash(10)
    num = 0
    for i in range (5):
        py()
        slash(10 - num)
        num += 2
    plus_line()
    print()
    print("Now only $50!")
    
main()
