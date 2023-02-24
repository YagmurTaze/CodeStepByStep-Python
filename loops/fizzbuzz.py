max = int(input("Max value? "))
for i in range (1, max+1):
    if i % 3 == 0 and not i % 5 == 0:
        print("Fizz",end = " ")
    elif not i % 3 == 0 and i % 5 == 0:
        print("Buzz",end = " ")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz",end = " ")
    else:
        print(i,end = " ")
    if i % 20 == 0:
        print()
