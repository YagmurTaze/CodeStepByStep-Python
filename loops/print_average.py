def print_average():
    num = 0
    sum = 0
    count = 0
    while True:
        num = int(input("Type a number: "))
        if num < 0:
            break
        sum += num
        count += 1
    if sum > 0:
        print("Average was",sum / count)
