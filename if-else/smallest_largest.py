def smallest_largest():
    nums = int(input("How many numbers do you want to enter? "))
    smallest = 999999
    largest = 0
    for i in range (1, nums+1):
        num = int(input("Number " + str(i) + ": "))
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    print("Smallest =",smallest)
    print("Largest =",largest)
