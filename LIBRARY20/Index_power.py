# def index_power(l, i):
#     try:
#         return l[i]**i
#     except:
#         return -1
#     pass

def index_power(l, i):
    return l[i]**i if i < len(l) else -1

index_power = lambda l,i: l[i]**i if i < len(l) else -1

print index_power([1, 2, 3, 4], 2) == 9
print index_power([1, 3, 10, 100], 3) == 1000000
print index_power([0, 1], 0) == 1
print index_power([1, 2], 3) == -1
