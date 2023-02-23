def biggest_and_smallest():
    nums = int(input("How many numbers do you want to enter? "))
    smallest = 999999
    biggest = 0
    for i in range (nums):
        num = int(input("Next number? "))
        if num < smallest:
            smallest = num
        if num > biggest:
            biggest = num
       
    print("Biggest =",biggest)
    print("Smallest  =",smallest)
