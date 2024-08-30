def second_half_letters(st):
    count = 0
    st = st.upper()
    for i in range (len(st)):
        if ord(st[i]) > 77 and ord(st[i]) < 91:
            count += 1
    return count