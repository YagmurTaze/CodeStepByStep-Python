def longest_name(num):
    max = 0
    longest = ""
    for i in range (1, num+1):
        name = input("name #" + str(i) + "? ")
        if len(name) > max:
            max = len(name)
            longest = name
    longest = longest[0].upper() + longest[1:].lower()
    print(longest + "'s","name is longest")
    if num >1 and len(name) == max:
        print("(There was a tie!)")
