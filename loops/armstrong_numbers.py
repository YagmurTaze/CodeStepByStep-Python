def armstrong_numbers(n):
    if n <= 0:
        return 
    start = 10**(n-1)
    end = 10**n
    if n == 1:
            print(0,end=" ",sep=" ")
    for i in range (start,end):
        sum = 0
        temp = i
        while(temp > 0):
            dig = temp % 10
            sum += dig**n
            temp = temp // 10
        if i == sum:
            print(i,end=" ",sep=" ")
