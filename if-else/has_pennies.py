def has_pennies(cents):
    nickels_only = cents % 5 == 0
    return not nickels_only
