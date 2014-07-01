V = "aeiouy"
C = "bcdfghjklmnpqrstvwxz"

def translate(m):
    n, g, rez = [[x for x in word] for word in m.split()], [' ', ' '],  []
    def c_w(l):
        if len(l) == 0:
            rez = "".join(x for x in g if x != ' ')
            del g[2:]
            return rez
        else:
            g.append(l[0])
            if (g[-2] in C) and (l[0] in V):
                g.pop()
                g.append(' ')
            if g[-3] == g[-2] == g[-1]:
                g[-2:]=[]
                g.append(' ')
            return c_w(l[1:])
    return " ".join([c_w(x) for x in n])


# import re,functools
# translate=functools.partial(re.sub,r"(\w)(\1\1|.)",r"\1")

# import re
# def translate(phrase):
#     for i in 0,1:
#         phrase = re.sub(r"(([[^. ].)]\)1[\.1]"[i::2].replace('.',"aeiouy"), r"\1", phrase)
#     return phrase

# translate=lambda s:s and s[0]+translate(s[1+(s[0]!=' ')+(s[0]in'aeiouy'):])

# def translate(s):
#     r = ''
#     while s:
#         c = s[0]
#         r += c
#         s = s[c.isalpha()+(c in'aeiouy')+1:]
#     return r

# def translate(phrase):
#     for ch in "aeiouy":
#         phrase = phrase.replace(ch*3, ch*2)
#     return ' '.join([''.join(n[::2]) for n in phrase.split(' ')])

print translate("hieeelalaooo")
print translate("hoooowe yyyooouuu duoooiiine")
print translate("aaa bo cy da eee fe")
print translate("sooooso aaaaaaaaa")
