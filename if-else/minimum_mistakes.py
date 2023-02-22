def main():
    a = 7
    b = 42
    minimum(a, b)

def minimum(a, b):
    smaller = 0
    if a < b:
        smaller = a
        print("a is the smallest!")
    else:
        smaller = b
        print("b is the smallest!")
    return smaller

main()
