import re


def checkio(text):
    pattern = r'^([aeiouy][bcdfghjklmnpqrstvwxz])+[aeiouy]?$|^([bcdfghjklmnpqrstvwxz][aeiouy])+[bcdfghjklmnpqrstvwxz]?$'
    listr = filter(lambda x: re.match(pattern, x),
                   re.split(r'[,. ]+', text.lower().strip('?!;')))
    return len(listr)

# puzzle:
# import re
# checkio=lambda t:sum(any(all('@'<c and j^(c in'aeiouyAEIOUY')^i&1
# for i,c in enumerate(w))for j in(0,1))for w in re.findall(r"\w\w+",t))


print checkio(u"My name is ...")
print checkio(u"Dog,cat,mouse,bird.Human.")
print checkio("Hello world")
print checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?")
