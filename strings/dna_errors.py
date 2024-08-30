def dna_errors(st1, st2):
    error = 0
    shorter_str = ""
    
    if not len(st1) == len(st2):
        if len(st1) < len(st2):
            shorter_str =  st1
            error += len(st2) - len(st1)
        else:
            shorter_str =  st2
            error += len(st1) - len(st2)
    else:
        shorter_str = st1
            
    for i in range (len(shorter_str)):
        if st1[i] == "A" and st2[i] == "T" or st1[i] == "T" and st2[i] == "A" or st1[i] == "G" and st2[i] == "C" or st1[i] == "C" and st2[i] == "G":
            continue
        elif st1[i] == "-" or st2[i] == "-":
            error += 1
        else:
            error += 2
        
    return error