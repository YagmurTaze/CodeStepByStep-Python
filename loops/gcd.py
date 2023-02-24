#there was a recursion limit. So...

def gcd(num1, num2):
    num1 = abs(num1)
    num2 = abs(num2)
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    if num1 < num2:
        (num1,num2) = (num2,num1)
    while num2 != 0:
        if(num1%num2) == 0:
            return num2
        if num1 == 0:
            return num2
        elif num2 == 0:
            return num1
        temp = num1
        num1 = num2
        num2 = temp % num2 
