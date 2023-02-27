def space(num):
    print(" " * num,end="")
    
def pipe_sizetimes():
    for i in range (SIZE):
        space(SIZE * 3)
        print("||")
        
def dots():
    num = 0
    for i in range (SIZE):
        space(SIZE * 3 - 3 - num)
        print("__/" + ":" * num + "||" +":" * num+"\__")
        num += 3

def slashs():
    num = 2
    for i in range (SIZE):
        space(num - 2)
        print("\_/" + "\/" * (3*SIZE-num) + "\_/")
        num += 2

def line():
    print("|" + "\"" * (SIZE * 6) + "|")
    
def perc():
    for i in range (SIZE*SIZE):
        space(SIZE * 2 + 1)
        print("|" + "%" * int(SIZE-2) + "||" + "%" * int(SIZE-2) + "|")
                 
def main():
    pipe_sizetimes()
    dots()
    line()
    slashs()
    pipe_sizetimes()
    perc()
    dots()
    line()
        
main()
