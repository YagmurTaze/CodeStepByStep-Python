def days_in_month(month):
    if month == 2:
        return 28
    elif month < 8:
        if month % 2 == 0:
            return 30
        else: return 31
    else:
        if month % 2 == 0:
            return 31
        else: return 30
        
#another way
def days_in_month(month):
    if month == 2:
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else: return 31
