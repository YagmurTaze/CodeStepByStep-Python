def first_digit(num):
    if num < 0 :
        num = abs(num)
    while num > 0:
        dig = num % 10
        num = num // 10
    return dig
