def convert_to_alt_caps(str):
    new_str = ""
    flag = False
    for i in range (0,len(str)):
        if str[i] == " ":
            new_str += str[i]
        elif flag == False:
            new_str += str[i].lower()
            flag = True
        else:
            new_str += str[i].upper()
            flag = False
    return new_str