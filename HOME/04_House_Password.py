import re
listo = ('aaaa5aaDaaa')


def check(listo):
    # if not listo.islower():
    #     print "[OK] contains [A-Z]"
    # else:
    #     print "[NO] CAPS"
    # if len(listo) >= 10:
    #     print "[OK] len OK"
    # else:
    #     print "[NO] len"
    # pattern = r'[a-z]*[A-Z][A-Za-z]*'
    # if re.match(pattern, listo):
    #     print "OK"
    # else:"
    #     print "EE
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.{10,}).+$'
    if re.match(pattern, listo):
        print "[OK] Password is strong"
    else:
        print "[NO] Password is weak"
check(listo)
