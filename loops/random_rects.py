def random_rects():
    rect = int(input("How many rectangles? "))
    area = 0
    for i in range (1, rect+1):
        width = int(input("Width "+ str(i) + "? "))
        height = int(input("Height " + str(i) +"? "))
        for i in range(height):
            print("*" * (width))
        area += width * height
    print("Total area:",area)
