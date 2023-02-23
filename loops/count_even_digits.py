def count_even_digits(num, dig):
    count = 0
    for i in range(dig):
        last = num % 10
        if last % 2 == 0:
            count += 1
        num = num // 10
    return count
