def plus_line():
    print("+",end="")
    print("-" * (SIZE * 3),end="")
    print("+",end="")

def py():
    str = "How to Code in Python "
    print("|",end="")
    print(" " * int((( 3*SIZE ) - len(str)) / 2) ,end="")
    print(str,end="")
    print(" " * int((( 3*SIZE ) - len(str)) / 2) ,end="")
    print("|",end="")

def space(num):
    print(" " * num,end="")
    
def slash(num):
    print("/" * num)
     
def us_slash_3():
    print("___/",end="")

def us_slash_2(num):
    print("__/" * num ,end="")

def price():
    print("Now only $" + str(SIZE * 5) + "!")
    
def main():
    num = 0
    print(" " * (SIZE + 1),end="")
    plus_line()
    print()
    for i in range (1,SIZE + 1):
        space((SIZE + 1) - i)
        print("/",end="")
        space(SIZE * 3 - 3 - num)
        num += 3
        us_slash_3()
        us_slash_2(i-1)
        slash(i-1)
    plus_line()
    slash(SIZE)
    num = 0
    for i in range (int(SIZE / 2)):
        py()
        slash(SIZE - num)
        num += 2
    plus_line()
    print()
    price()
    
main()
