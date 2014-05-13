#1
def checkio(numbers_array):
    return sorted(numbers_array, key= abs)

print checkio((-20, -5, 10, 15))


#2
checkio = lambda numbers_array: sorted(numbers_array, key=abs)
print checkio((-20, -5, 10, 15))
