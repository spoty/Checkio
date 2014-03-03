def checkio(number):
    return reduce(lambda x, y: x*y, [int(i) for i in str(number) if i != "0"])

print checkio(125045)


