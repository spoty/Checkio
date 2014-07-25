def swapsort(t):
    t, r = list(t), []
    while not t == sorted(t):
        for i in range(len(t)-1):
            if t[i] > t[i+1]:
                t[i+1], t[i] = t[i], t[i+1]
                r.append(`i`+`i+1`)
    return ','.join(r) if r else ""


print swapsort((6, 4, 2))
print swapsort((1, 2, 3, 4, 5))
print swapsort((1, 5, 8, 9, 3))
print swapsort((1, 2, 3, 5, 3))
print swapsort((9,1,1,1,1,1,1,1,1,1,))
# swapsort((4,6,5,2,6,1,))
# swapsort((3,2,7,2,3,7,9,6,9,))
# swapsort((5,8,5,3,7,8,1,5,1,4,))
# swapsort((7,1,3,8,5,9,7,))
# swapsort((1,8,7,9,6,4,))
# swapsort((3,7,7,6,7,1,3,3,4,9,))

