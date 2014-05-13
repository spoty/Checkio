

# def checkio(teleports_str):
#     teleports_map = [tuple(sorted([int(x), int(y)]))
#                      for x, y in teleports_str.split(",")]
#     print teleports_map


# print checkio("12, 23, 34, 45, 56, 67, 78, 81")


s = "12,23,34,45,56,67,78,81,13"
rez = [e for e in s.split(',')]
print rez

# rez = [[int(x)] for x in teleports_str.split(",")]
# print rez

# mydict = dict(e for e in s.split(','))
# print mydict




# years_dict = dict()


# for line in s:
#     if line[0] in years_dict:
#         # append the new number to the existing array at this slot
#         years_dict[line[0]].append(line[1])
#     else:
#         # create a new array in this slot
#         years_dict[line[0]] = [line[1]]

for x in rez:

