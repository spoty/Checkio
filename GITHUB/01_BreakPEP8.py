from string import maketrans as m

def twist(t):
    t = ' '.join(x[::-1] for x in t.split()).swapcase()
    for x in t.split():
        if x[0] in "!?":
            t = t.replace(x, x[1:]+x[0])
    mt= m(',.!?)(}{][><#@;:0123456789', '.,?!)(}{][><@#:;9876543210')
    return t.translate(mt)



#print "....".translate(maketrans(u',.', u'.,'))




print twist("Hello World!") == "OLLEh DLROw?"
print twist("I`m 1st") #== "i`M 8TS"
print twist("How are you? 905th.") #== "WOh ERA UOY! 094HT,"
print twist("The code - ([{<;#>}])") #== "EHt EDOC - )]}>:@<{[("
print twist("EMAIL        a@b.ru") #== "liame A#B,UR"
print twist(";-) 0_0 @__@") #== ":-( 9_9 #__#"
