def space(num):
    print(" " * num,end="")
    
def plus_line():
    print("+",end="")
    print("-" * 30,end="")
    print("+",end="")

def part1():
    num = 0
    for i in range (1,11):
        space(11 - i)
        print("/",end="")
        space(27 - num)
        num += 3
        us_slash_3()
        us_slash_2(i-1)
        slash(i-1)
        
def part2():
    num = 0
    for i in range (5):
        py()
        slash(10 - num)
        num += 2

def py():
    str = "How to Code in Python "
    print("|" + " " * 4 + str + " " * 4 + "|", end = "")
        
def slash(num):
    print("/" * num)
     
def us_slash_3():
    print("___/",end="")

def us_slash_2(num):
    print("__/" * num ,end="")

def price():
    print("Now only $50!")
    
def main():
    space(11)
    plus_line()
    print()
    part1()
    plus_line()
    slash(10)
    part2()
    plus_line()
    print()
    price()
    
main()
