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




#Be aware of all, any and map:
if isdigit(a) and isdigit(b) and isd
igit(c)
if all(map(isdigit,[a,b,c]))
# filter(function, iterable) returns a list of all the elements of iterable`
# for which function is a True-y value and a non-empty list is True-y,
# so this can be shortened further to
if filter(isdigit,[a,b,c])





# If you need to import a lot of modules you can reassign __import__ to something
# shorter, this also has the advantage of being able to name imports anything you
# want.
i=__import__;s=i('string');x=i('itertools');



# we can use
~
# as negator, if we take -1 as True
#  a ~a
#  0 -1
# -1  0
# Compare
while~a:
while not a:






# To find the all the indexes of a certain element in a list l, use
filter(lambda x:l[x]==element,range(len(l)))
# To find the next index after a certain index:
l[:index].index(element)
# To find the nth index:
list(filter(lambda x:l[x]==element,range(len(l))))[n]





# Although python doesn't have switch statements, you can emulate them with
# dictionaries. For example, if you wanted a switch like this:
switch (a):
    case 1:
        runThisCode()
        break
    case 2:
        runThisOtherCode()
        break
    case 3:
        runThisOtherOtherCode()
        break
# You could use if statements, or you could use this:
exec{1:"runThisCode()",2:"runThisOtherCode()",3:"runThisOtherOtherCode"}[a]
# To support a default value:
exec{1:"runThisCode()"}.get(a,"defaultCode()")
# One other advantage of this is that if you do have redundancies, you could
#  just add them after the end of the dictionary:
exec{'key1':'code','key2':'code'}[key]+';codeThatWillAlwaysExecute'
# And if you just wanted to use a switch to return a value:
def getValue(key):
    if key=='blah':return 1
    if key=='foo':return 2
    if key=='bar':return 3
    return 4
# You could just do this:
getValue=lambda key:{'blah':1,'foo':2,'bar',3}.get(key,4)

