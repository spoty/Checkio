from collections import Counter
def checkio(first, second):
    return ",".join(sorted([x for x, y in Counter(str(first +","+ second).split(',')).items() if y >1]))

# def checkio(first, second):
#     same_words = set(first.split(',')).intersection(second.split(','))
#     return ','.join(sorted(same_words))

print checkio(u"hello,world", u"hello,earth,world")
