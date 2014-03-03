def checkio(array):
    if not array:
        return 0

    list = []
    for item in array:
        if array.index(item) % 2 ==0:
            list.append(item)
    return (sum(list)*array[(len(array)-1)])


print checkio([-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41])


list2 = [-37, -36, 92]
print sum(list2)
