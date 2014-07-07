def checkio(l, m=''.join):
    c = lambda s: [x[0] for x in s if len(set(x)) == 1 and x[0] != '.'] or 'D'
    return m(c(l + map(None, *l) + [m(l)[::4], m(l)[2:-1:2]]))[0]


# print checkio([
#     "X.O",
#     "XX.",
#     "XOO"]) == "X"
# print checkio([
#     "OO.",
#     "XOX",
#     "XOX"]) == "O"
# print checkio([
#     "OOX",
#     "XXO",
#     "OXX"]) == "D"
# print checkio(["OXO","XOX","OXO"])
print checkio(["...", "XXX", "OO."])
