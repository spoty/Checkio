"""
If you're using a built-in function repeatedly, it might be more
space-efficient to give it a new name:
"""
r = range
for x in r(10):
    for y in r(10):
        print x, y


"""
Conditionals can be lengthy. In some cases, you can replace a simple
conditional with (a,b)[condition]. If condition is true, then b is returned.
"""
# Compare
if a < b:
    return a
return b
# To this
return(b, a)[a < b]

# or
a if a < b else b
# or
P and [A] or [B]


# Use
a = b = c = 0
# instead of
a, b, c = 0, 0, 0

# Use
a, b, c = '123'
# instead of
a, b, c = '1', '2', '3'


# A great thing I did once (and that only python allows) is
if 3 > a > 1 < b < 5:
    foo()
# instead of
if a > 1 and b > 1 and 3 > a and 5 > b:
    foo()


# Using that everything is comparable in Python 2, you can also
# avoid the and operator this way. For example, if a, b, c and d are integers,
if a < b and c > d:
    foo()
# can be shortened by one character to
if a < b < [] > c > d:
    foo()
# This uses that every list is larger than any integer.
# If c and d are lists, this gets even better
if a < b < c > d:
    foo()


# nstead of range(x), you can use the * operator on a list of anything, if
# you don't actually need to use the value of i:
for i in[1] * 8:
# as opposed to
for i in range(8):
# note you save yet another character by omitting the space before [
# if you need to do this more than twice, you could assign any iterable
# to a variable, and multiply that variable by the range you want:
r = [1]
for i in r * 8:
    pass
for i in r * 1000:
    pass
# as opposed to:
r = range
for i in r(8):
    pass
for i in r(1000):
    pass
# edit: saving 1 more character, you can use tuple notation instead of
# a character or list:
r = 1,
for i in r * 8:
    pass
# but that won't work if you only need to use it once:
for i in 1, *8:
    pass  # this is invalid syntax


# convert boolen to integer
x = True
print x, +x
