def check_connection(network, first, second):
    l = lambda m: sum([c.split('-') for c in network if m in c], [])
    d, f = l(first), [first]
    for n in d:
        if n not in f:
            d.extend(l(n))
            f.append(n)
    return second in set(d)



print check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3")
print check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "super", "scout2") == True, "Super Scout"
print check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False, "I don't know any scouts."


# def check_connection(network, first, second):
#     d = sum([c.split('-') for c in network if first in c], [])
#     f = [n for n in d if n == first]
#     for n in d:
#         if n not in f:
#             d.extend(sum([c.split('-') for c in network if n in c], []))
#             f.append(n)
#     return second in set
