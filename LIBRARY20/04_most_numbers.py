def checkio(*args):
    if args:
        return (max(args) - min(args))
    else:
        return 0



# assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
# assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
# assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
# assert almost_equal(checkio(), 0, 3), "Empty"

print checkio(1.154, 2, 30.158)




