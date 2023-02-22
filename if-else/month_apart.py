def month_apart(month1, day1, month2, day2):
    if month1 == month2:
        return False
    elif abs(month1-month2) > 1:
        return True
    else:
        if month1 > month2:
            return day1 >= day2
        else:
            return day2 >= day1
