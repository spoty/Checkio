from datetime import date

def days_diff(d1,d2):
    return abs((date(*d1)-date(*d2)).days)

print days_diff((1982, 4, 19), (1982, 4, 22))




