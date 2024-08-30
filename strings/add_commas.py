def add_commas(str):
    new = ''
    for i in range(len(str)):
        if i > 0 and (len(str) - i) % 3 == 0:
            new += ','
        new += str[i]
    return new