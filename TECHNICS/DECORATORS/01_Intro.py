"""
Example 1: Tagging
"""

def paragraphize(inputFunction):
   def newFunction():
      return "<p>" + inputFunction() + "</p>"
   return newFunction

@paragraphize
def getText():
   return "Here is some text!"

print getText()

"""
Example 2: Printing arguments
"""

def printArgsFirst(f):
   def newFunction(*args):
      print(args)
      return f(*args)
   return newFunction

@printArgsFirst
def randomFunction(x, y, z):
   return x + y + z

print randomFunction(1,2,3)


"""
Example 3: Memoize
"""

def memoize(f):
    cache = {}
    def memoizedFunction(a):
      if a not in cache:
         cache[a] = f(a)
      return cache[a]
    return memoizedFunction

@memoize
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print fib(100)

# fibTable = {1:1, 2:1}
# def fib(n):
#    if n <= 2:
#       return 1
#    if n in fibTable:
#       return fibTable[n]
#    else:
#       fibTable[n] = fib(n-1) + fib(n-2)
#       return fibTable[n]
