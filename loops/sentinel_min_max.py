num = int(input("Type a number (or -1 to stop): "))
max = num
min = num
while num != -1:
    if num > max:
        max = num
        
    elif num < min:
        min = num
    num = int(input("Type a number (or -1 to stop): "))
if max != -1:    
    print("Maximum was",max)
    print("Minimum was",min)
