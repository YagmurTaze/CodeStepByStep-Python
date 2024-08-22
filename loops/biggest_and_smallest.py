def biggest_and_smallest():
    nums = int(input("How many numbers? "))
    num = int(input("Next number? "))
    smallest = num
    biggest = num
    for i in range (nums-1):
        num = int(input("Next number? "))
        if num < smallest:
            smallest = num
        if num > biggest:
            biggest = num
       
    print("Biggest =",biggest)
    print("Smallest =",smallest)
    
biggest_and_smallest()
