def has_midpoint(int1, int2, int3):
    sum = int1 + int2 + int3
    div = sum / 3
    if not sum % 3 == 0:
        return False
    elif div ==  int1 or int2 or int3:
        return True
    return False
