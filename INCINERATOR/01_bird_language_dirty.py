V = "aeiouy"
C = "bcdfghjklmnpqrstvwxz"

def translate(m):
    n = [[x for x in word] for word in m.split()]
    g = [' ', ' ']
    rez = []
    # print n[1]
    def c_w(l):
        if len(l) == 0:
            rez = "".join(x for x in g if x != ' ')
            # print rez
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
                # g.append(' ')
            # print g, l[0]
            return c_w(l[1:])
    # print c_w(n[0])
    print [c_w(x) for x in n]
    # print rez
    # g = "".join(g).replace(" ", '')
    # h = ['','']
    # def www(g):
    #     if len(g) == 0:
    #         return h
    #     else:
    #         h.append(g[0])
    #         if h[-3] == h[-2] == h[-1]:
    #             h[-2:]=[]
    #         return www(g[1:])
    # www(g)
    # return "".join(h).replace(" ", '')


print translate("hieeelalaooo")
print translate("hoooowe yyyooouuu duoooiiine")
print translate("aaa bo cy da eee fe")
print translate("sooooso aaaaaaaaa")
