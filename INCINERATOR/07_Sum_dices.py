def dice(k):
    d = 6*[1]
    for i in range(k-1):
        t = 5*[0] + d + 5*[0]
        d = [sum(t[i:i+6]) for i in range(len(t)-5)]
    return d

def t(k,n):
         return dice(k)[n-k]

print dice(3)

print t(2,10)
