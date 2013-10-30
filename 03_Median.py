def checkio(data):
    soort = sorted(data)
    lenn = len(soort)
    if not lenn % 2:
        return ((soort[int(lenn/2)] + soort[int(lenn/2-1)]) / 2.0)
    return soort[int(lenn/2)]
