COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
import textwrap
def cowsay(s):
    print len(s.split())
    if len(s.split()) != 1:
        s = ' '.join(s.split())
    f = textwrap.wrap(s,39)
    d = len(f[0])
    f = [x.ljust(d) for x in f]
    top =  " "+"_"*(d +2)
    h = []
    for i, x in enumerate(f):
        n = "{["+ str(i) +"]}"
        if len(f) == 1: h.append("< "+str(n.format(f))+" >")
        elif (i == 0): h.append("/ "+n.format(f)+" \\")
        elif (i == len(f)-1): h.append("\\ "+str(n.format(f))+" /")
        else: h.append("| "+str(n.format(f))+" |")
    bottom =  " "+"-"*(d +2)
    return str("\n"+top+"\n"+"\n".join(h)+"\n"+bottom+COW)



# print cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
print cowsay(' a')
print cowsay('a ')
print cowsay("spaces inside")
