import re


def checkio(text):
    pattern = r'^([aeiouy][bcdfghjklmnpqrstvwxz])+[aeiouy]?$|^([bcdfghjklmnpqrstvwxz][aeiouy])+[bcdfghjklmnpqrstvwxz]?$'
    listr = filter(lambda x: re.match(pattern, x),
                   re.split(r'[,. ]+', text.lower()))
    return len(listr)


print checkio(u"My name is ...")
print checkio(u"Dog,cat,mouse,bird.Human.")
print checkio("Hello world")
