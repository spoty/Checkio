def checkio(array):
    if not array:
        return 0

    listo = []
    for item in array:
        if array.index(item) % 2 ==0:
            listo.append(item)
    return sum(listo)*array[(len(array)-1)]
