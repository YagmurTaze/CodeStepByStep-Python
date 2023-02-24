print("This program lists the Fibonacci sequence.")
max = int(input("Max value? "))
prev = 0
next = 1
print(prev,end="")
while next <= max:
    print(",",next,end="")
    temp = next
    next = prev + next
    prev = temp    
