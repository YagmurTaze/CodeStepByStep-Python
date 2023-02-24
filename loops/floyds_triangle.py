def floyds_triangle(k):
    count = 1
    for i in range (k + 1):
        for j in range (i):
            print(count,end = " ")
            count += 1
        print()
