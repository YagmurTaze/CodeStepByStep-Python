def contribution(count1, count2, sum, total):
    times = int(input("Is your money multiplied 1 or 2 times? "))
    donation = int(input("And how much are you contributing? "))
    
    if times == 1:
        sum += donation
        count1 += 1
    elif times == 2:
        sum += 2 * donation
        count2 += 1
    total += donation
