query = input("What is your name? ")

name_arr = query.split()

name = name_arr[0]
last_name = name_arr[1]

rhyme = "{}, {}, bo-B{}\n" \
        "Banana-fana fo-F{}\n" \
        "Fee-fi-mo-M{}\n" \
        "{}!\n\n" \
        "{}, {}, bo-B{}\n" \
        "Banana-fana fo-F{}\n" \
        "Fee-fi-mo-M{}\n" \
        "{}!".format(
            name, name, name[1:],
            name[1:], name[1:], name.upper(),
            last_name, last_name, last_name[1:],
            last_name[1:], last_name[1:], last_name.upper()
        )

print(rhyme)