from datetime import date, timedelta


def checkio(fromdate, todate):
#     """ This Function counts weekends (in days)
#     DOCs: https://docs.python.org/2/library/datetime.html

#     My solution isn't very good, time need for computation
#     is increasing.
#     READ: http://en.wikipedia.org/wiki/Computational_complexity_theory
#     """
    relevant_days = (fromdate - timedelta(1) + timedelta(x + 1) for x in xrange((todate-fromdate).days + 1))
    return sum(1 for day in relevant_days if day.weekday() > 4)


print checkio(date(2013, 9, 18), date(2013, 9, 23))
print checkio(date(2013, 1, 1), date(2013, 2, 1))
print checkio(date(2013, 2, 2), date(2013, 2, 3))

"""
From comments:
http://en.wikipedia.org/wiki/Iverson_bracket

def checkio(d1, d2):
    w1, w2 = d1.weekday(), d2.weekday()
    count = (d2 - d1).days // 7 * 2
    while True:
        count += w2 > 4
        if w1 == w2: return count
        w2 = (w2 - 1) % 7



def checkio(fromdate, todate):
    return sum(1 for d in range((todate - fromdate).days + 1)
        if (fromdate + timedelta(d)).weekday() in [5, 6])

But a more important point: bool can count.
BDFL intentionally made bool a subclass of int.

So,
    sum(cond for iter)
is nicer than
    sum(1 for iter if cond)

def checkio(fromdate, todate):
    return sum(((fromdate + timedelta(d)).weekday() in [5, 6]) for d in range((todate - fromdate).days + 1))
"""

