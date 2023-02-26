def print_factors(num):
    print("1 ",end="")
    for i in range (2,num+1):
        if num % i == 0:
            print("and",i,end=" ")

