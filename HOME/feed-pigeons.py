def checkio(number):
    x = 0
    n = 1
    while number > 0:
        x =  x + n
        n = n + 1
        number = number - x
        print "before SUPPLY: %s, BIRDS: %s, after SUPPLY: %s" % (number + x, x, number)
        #print "N %s" % n
        if (number + x) < x:
            if (number + x) < (x - n):
                print x - (n-1)
                return x - (n-1)
            else:
                print number + x
                return number + x
        if number == 0:
            print x
            return x

checkio(50)
