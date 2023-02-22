def even_sum_max():
    num = int(input("how many integers? "))
    sum = 0
    max = 0
    for i in range (num):
        next = int(input("next integer? "))
        if next % 2 == 0:
            sum += next
            if next > max:
               max = next
    print("even sum =",sum)
    print("even max =",max)
