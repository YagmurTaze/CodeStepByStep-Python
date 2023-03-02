def space(num):
    print(" " * num,end="")
    
def head_tail():
    num = 2 * SIZE - 1
    for i in range (1, num + 1):
        space(num + 1 - i)
        print("/" * i + "**" + "\\" * i)
             
def line():
    print("+" + "=*" * (SIZE * 2) + "+")
        
def body1():
    num = 1
    for i in range (1, SIZE + 1):
        print("|" + "." * (SIZE - i) + "/\\" * i + "." * ((SIZE - 1) * 2 + 1 - num) + "/\\" * i + "." * (SIZE -i) + "|")
        num += 2
    num = 0
    for j in range (SIZE):
        print("|" + "." * j + "\\/" * (SIZE - j) + "." * (num) + "\\/" * (SIZE - j) + "." * j + "|")
        num += 2
        
def body2():
    num = 0
    for j in range (SIZE):
        print("|" + "." * j + "\\/" * (SIZE - j) + "." * (num) + "\\/" * (SIZE - j) + "." * j + "|")
        num += 2
    num = 1
    for i in range (1, SIZE + 1):
        print("|" + "." * (SIZE - i) + "/\\" * i + "." * ((SIZE - 1) * 2 + 1 - num) + "/\\" * i + "." * (SIZE -i) + "|")
        num += 2
        
def main():
    head_tail()
    line()
    body1()          
    line()
    body2()          
    line()
    head_tail()
        
main()
