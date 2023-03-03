def swap_digit_pairs(n):
    res = 0
    x = 1
    while n > 0:
            dig1 = n % 10 
            n = n // 10

            if n == 0:
                res += dig1 * x
                break

            dig2 = n % 10
            n = n // 10

            res += x * (10 * dig1 + dig2)
            x *= 100
            
    return res
