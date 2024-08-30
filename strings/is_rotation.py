def is_rotation(s1,s2):
    new_str = s1 + s1
    if not len(s1) == len(s2):
        return False
    if s2 in new_str:
        return True
    return False