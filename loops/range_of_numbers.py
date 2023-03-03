def range_of_numbers(num1, num2):
    if num2 > num1:
        for i in range (num1, num2+1):
            print(i,end=" ")
    else:
        for i in range (num1, num2 -1, -1):
            print(i,end=" ")
