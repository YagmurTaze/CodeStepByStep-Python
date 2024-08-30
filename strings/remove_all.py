def remove_all(st,find):
    new_str = ''
    for i in range (len(st)):
        if find == st[i]:
            new_str += ""
        else:
            new_str += st[i]
    return new_str