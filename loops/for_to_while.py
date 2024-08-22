# a.
print("a.")
maxs = 5 
n = 1
while n < maxs+1:
    print(n)
    n+=1
print()

# b.
print("b.")
total = 25
number = 1
while number <= (total // 5) + 2:
    total -= number
    print(total, number)
    number += 1
print()

# c.
print("c.")  
i=1
while i < 3:
    j = 1
    while j < 4:
        k = 1
        while k < 5:
            print("*", end="")
            k += 1
        print("!", end="")
        j += 1
    print()
    i += 1    
