COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
import re
import textwrap
def cowsay(s):
    f = textwrap.wrap(s,39)
    if len(s)>39:
        f = textwrap.wrap(' '.join(s.split()),39)
        d = max([len(x) for x in f])
        f = [x.ljust(d) for x in f]
    else:
        d, f[0] = len(re.sub('\s+', ' ', s)), re.sub('\s+', ' ', s)
    h = []
    m = lambda lb,rb: h.append(lb+str(n.format(f))+rb)
    for i, x in enumerate(f):
        n = '{['+ str(i) +']}'
        if len(f) == 1: m('< ', ' >')
        elif (i == 0): m('/ ', ' \\')
        elif (i == len(f)-1): m('\\ ', ' /')
        else: m('| ', ' |')
    top, bottom =  '\n'+' '+'_'*(2+d)+'\n', '\n'+' '+'-'*(2+d)
    return str(top+'\n'.join(h)+bottom+COW)



print cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
print cowsay(' a')
print cowsay('a ')
print cowsay('looooooooooooooooooooooooooooooooooooong')
print cowsay('    c    ')
print cowsay('A longtextwithonlyonespacetofittwolines.')
# print cowsay('l')
# print len('looooooooooooooooooooooooooooooooooooong')
# print cowsay('spaces inside')
