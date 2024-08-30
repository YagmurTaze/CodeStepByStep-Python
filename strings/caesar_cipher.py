msg = input("Your message? ") 
key = input("Encoding key? ") 

msg = msg.upper()
cipher_msg = ""

for i in range (0,len(msg)):
    if msg[i] == " ":
        cipher_msg += " "
    elif ord(msg[i]) < 64 or  ord(msg[i]) > 91:
        cipher_msg += msg[i]
    else:
        cipher_msg += chr((ord(msg[i]) - 65 + int(key)) % 26 + 65)

print(cipher_msg)