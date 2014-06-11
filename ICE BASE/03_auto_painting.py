def checkio(capacity, number):
    items = "".join(str(x) for x in range(number)*2)
    step = min(capacity, number)
    return ",".join(items[x:x+step] for x in range(0, len(items), step))


print checkio(2, 3)  # "01,12,02"
print checkio(6, 3)  # "012,012"
print checkio(3, 6)  # "012,012,345,345"
print checkio(1, 4)  # "0,0,1,1,2,2,3,3"
print checkio(2, 5)  # "01,01,23,42,34"


"""
Other's solutions:
"""
# checkio=lambda K,N:','.join(("0123456789"[:N]*2)[i:i+min(N,K)]for i in range(0,2*N,min(N,K)))
