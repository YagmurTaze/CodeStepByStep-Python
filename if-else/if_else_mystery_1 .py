def if_else_mystery_1(x, y):
    z = 4
    if z <= x:
        z = x + 1
    else:
        z = z + 9
    if z <= y:
        y += 1
    print(z, y)
    
   """
   if_else_mystery_1(3, 20) = 13 21
   if_else_mystery_1(4, 5)  = 5 6
   if_else_mystery_1(5, 5)  = 15 5
   if_else_mystery_1(6, 10) = 7 11
   """
