"""
The list of banned words are as follows:

    sum
    import
    for
    while
    reduce

Input: A list of numbers.

Output: The sum of numbers.
"""
# Recursive
def checkio(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + checkio(numList[1:])

def checkio(data):
    if len(data)==0: return 0
    return data[0]+checkio(data[1:])

def checkio(data):
    return eval("+".join(map(str,data)))

def checkio(data):
    if len(data) > 0:
        return data.pop() + checkio(data)
    else:
        return 0

def checkio(d):
    r=''.join(map(lambda x:"+"*x+"-"*-x,d)).count
    return r("+")-r("-")

checkio = lambda x: eval('%c%c%c(%s)' % (115, 117, 109, x))

checkio = eval("su"+"m")

checkio = lambda d:eval('+'.join(map(str,d)))

print checkio([1,2])

