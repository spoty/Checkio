def checkio(number):
    return len([int(i) for i in str((bin(number)[2:])) if i != "0"])
    # res = [int(i) for i in str((bin(number)[2:])) if i != "0"]
    # return reduce(lambda x,y: len(res), res)

print checkio(15)



