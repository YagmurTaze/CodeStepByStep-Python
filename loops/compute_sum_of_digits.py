num = int(input("Type an integer: "))
sum = 0
while(num > 0):
    dig = num % 10
    sum += dig
    num = num // 10
print("Digit sum is",sum)
