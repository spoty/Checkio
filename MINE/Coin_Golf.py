
# l=[10,2,2,1]

# # r = []
# # for i,_ in enumerate(l): r.append(map(sum, x(l, i+1)))
# # l = list(set(sum(r, [])))

# # print l
# # print [x for x in range(min(l),max(l)) if not x in l][0]

# x=__import__('itertools').combinations
# golf=lambda l:list(set(sum([map(sum,x(l,o+1))for o,_ in enumerate(l)],[])))

# print golf(l)
# print golf([10,2,2,1])
l = [1,1,1,1]
# print list(set(sum([map(sum,x(l,o+1))for o,_ in enumerate(l)],[])))

# x=__import__('itertools').combinations


golf=lambda l:[v for v in range(1,9*9)if not v in sum([map(sum,__import__('itertools').combinations(l,o+1))for o,_ in enumerate(l)],[])][0]
# print [list(__import__('itertools').combinations(l,o+1)) for o,_ in enumerate(l)]
print sum([map(sum,__import__('itertools').combinations(l,o+1))for o,_ in enumerate(l)],[])
print sum([map(sum,__import__('itertools').combinations(l,o))for o in range(1,11)],[])

# next()
# [][0]

# print golf([10,2,2,1]) == 6
# print golf([1,1,1,1]) == 5
# print golf([1,2,3,4,5]) == 16
# print golf([1,1,1,1,1,1,1,1,1,1]) == 11
# print golf([1,2,3,4,5,6,7,8,9]) == 46
# print golf([9,8,7,6,5,4,3,2,1]) == 46
# print golf([6,8,9,5,9,5,7,1,2,3]) == 56
# print golf([9,9,9,9,9,9,9,9,9,9]) == 1

# def golf(l):
#     m=list(set(sum([map(sum,x(l,o+1))for o,_ in enumerate(l)],[])))
#     print m
#     k=[v for v in range(1,max(l)+1)if not v in m]
#     return k[0] if k else m[-1]+1

# print golf([10,2,2,1])
# print golf([9,9,9,9,9,9,9,9,9,9])
golf=lambda l:[v for v in range(1,9*9)if not v in sum([map(sum,__import__('itertools').combinations(l,o))for o in range(11)],[])][0]
print golf(l)
def golf(l):r,o=[],1;exec'r.extend(map(sum,__import__("itertools").combinations(l,o)));o+=1;'*11;return[v for v in range(1,9*9)if not v in r][0]
print golf(l)


