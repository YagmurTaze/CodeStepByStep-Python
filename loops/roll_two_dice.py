d_sum = int(input("Desired sum: "))
sum = 0
while sum != d_sum:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    print(dice1,"and",dice2,"=",sum)
