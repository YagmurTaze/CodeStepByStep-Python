def digit_sum(num):
    sum = 0
    if num < 0:
        num = abs(num)
    while num > 0:
        dig = num % 10
        sum += dig
        num = num // 10
    return sum
