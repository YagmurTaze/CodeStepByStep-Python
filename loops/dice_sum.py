def dice_sum():
    num = int(input("Desired dice sum: "))
    sum = 0
    while sum != num:
        dice1 = random.randint(0,6)
        dice2 = random.randint(0,6)
        sum = dice1 + dice2
        print(dice1,"and",dice2,"=",sum)
