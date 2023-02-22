def median_of_3(n1, n2, n3):
    if n1 < n2:
        if n2 < n3:
            return n2
        elif n3 < n1:
            return n1
        else:
            return n3
    else:
        if n1 < n3:
            return n1
        elif n3 < n2:
            return n2
        else:
            return n3
