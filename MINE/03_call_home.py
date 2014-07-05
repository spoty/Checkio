from math import ceil


def total_cost(calls):
    d = {}
    for call in calls:
        if call[:10] not in d:
            d[call[:10]] = 0
        d[call[:10]] += int(ceil(float(call[20:]) / 60))
    return sum(x < 100 and x or x > 100 and 100 + (x - 100) * 2 for x in d.values())


def total_cost(calls):
    d = __import__('collections').defaultdict(int)
    for call in calls:
        d[call[:10]] += (int(call[20:]) + 59) // 60
    return sum(x + (x - 100) * (x > 100) for x in d.values())

from collections import Counter

def total_cost(calls):
    db = Counter()
    for call in calls:
        day, time, duration = call.split()
        db[day] += (int(duration) + 59) // 60
    return sum(min if min < 100 else 2*min-100 for min in db.values())


print total_cost(("2014-01-01 01:12:13 181",
                  "2014-01-02 20:11:10 600",
                  "2014-01-03 01:12:13 6009",
                  "2014-01-03 12:13:55 200",
                  "2014-01-03 12:13:55 2000"))
