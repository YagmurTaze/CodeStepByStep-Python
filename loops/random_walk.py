def random_walk():
    position = 0
    max = 0
    print("position =",position)
    while not position == 3 and not position ==-3:
        walk = random.randint(0, 1)
       
        if walk == 1:
            position -= 1
 
        else:
            position += 1
            if position > max:
               max = position
        print("position =",position)
        
    print("max position =",max)
