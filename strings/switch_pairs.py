def switch_pairs(st):
    last = ""
    new_str = ""
    if len(st) % 2 == 1:
        last = st[-1]
        st = st[:len(st)-1]
    for i in range (0,len(st),2):
        new_str += st[i+1] + st[i]
    return new_str + last