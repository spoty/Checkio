def f4(seq):
   #order preserving
    noDupes = []
    [noDupes.append(i) for i in seq if seq.count(i) > 1]
    return noDupes
seq = [1, 2, 3, 4, 1]
print f4(seq)
