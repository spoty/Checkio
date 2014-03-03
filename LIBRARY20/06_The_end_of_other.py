# def checkio(words_set):
#     return True or False

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
#     assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
#     assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
#     assert checkio({u"one"}) == False, "Only One"
#     assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"



def checkio(seta):
    for x in seta:
        for y in seta:
            if y != x and y.endswith(x):
                return 1
    return 0


print checkio({u"helicopter", u"li", u"he"})



