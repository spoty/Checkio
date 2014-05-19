l = [1, 2, 3, 4, 5, 6, 7, 8]
sort_1 = zip(l[::2], l[1::2])
print sort_1
# print [i for i in zip(l[::2], l[1::2])]

sort_2 = zip(l, l[1:])
print sort_2

sort_3 = l[::len(l)-1]
print sort_3


# ULOHA: Naprogramuje nieco taketo:

# def grouper(iterable, n, fillvalue=None):
#     "Collect data into fixed-length chunks or blocks"
#     # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
#     args = [iter(iterable)] * n
#     return zip_longest(*args, fillvalue=fillvalue)
