def enough_time_for_lunch(hour1, minute1, hour2, minute2):
    if hour2 < hour1:
        return False
    elif hour1 == hour2:
        dif = minute2 - minute1 
        if dif >= 45:
            return True
    else:
        if hour2 - hour1 > 1:
            return True
        else:
            dif = minute2 + (60 - minute1)
            if dif >=45:
                return True
            else: return False
