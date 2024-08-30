def same_dashes(st1, st2):
    d_num1 = st1.count("-")
    d_num2 = st2.count("-")
    
    if not d_num1 == d_num2:
        return False
    
    flag = 0
    for i in range (len(st1)):
        
        id1 = st1.find("-",flag,len(st1))
        id2 = st2.find("-",flag,len(st2))
        
        if not id1 == id2:
            return False
        flag = id1 + 1
        
    return True