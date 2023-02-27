def space(num):
    print(" " * num,end="")
    
def pipe_sizetimes():
    for i in range (4):
        space(12)
        print("||")
        
def dots():
    num = 0
    for i in range (4):
        space(9 - num)
        print("__/" + ":" * num + "||" +":" * num+"\__")
        num += 3

def slashs():
    num = 2
    for i in range (4):
        space(num - 2)
        print("\_/" + "\/" * (12-num) + "\_/")
        num += 2

def line():
    print("|" + "\"" * (24) + "|")
    
def perc():
    for i in range (16):
        space(9)
        print("|" + "%" * 2 + "||" + "%" * 2 + "|")
                 
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
