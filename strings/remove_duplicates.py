def remove_duplicates(st):
    if len(st) == 0:
        return ""
    
    new_str = st[0]
    for i in range (1,len(st)):
        if st[i] == st[i-1]:
            continue
        new_str += st[i]
    return new_str