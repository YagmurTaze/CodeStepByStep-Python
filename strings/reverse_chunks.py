def reverse_chunks(s, k):
    last = ""
    new_str = ""
    
    if not len(s) % k == 0:
        last = s[-(len(s) % k):]
        
    for i in range (0,len(s) - (len(s) % k) ,k):
        part = s[i:i+k]
        new_str += part[::-1]
        
    return new_str + last