print("Welcome to Piglet!")
ch = ""
sum = 0
while ch != "no":
    num = random.randint(1,6)
    if num == 1:
        print("You rolled a",num)
        print("You got 0 points.")
        break
    sum += num
    print("You rolled a",num)
    ch = input("Roll again? ")
if num !=1:
    print("You got " + str(sum) + " points.")
