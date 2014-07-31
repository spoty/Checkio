"""
Imagine you have a collection of N wines placed next to each other on a
shelf. For simplicity, let's number the wines from left to right as they are
standing on the shelf with integers from 1 to N, respectively. The price of the
i-th wine is pi (prices of different wines can be different).

Because the wines get better every year, supposing today is the year 1, on year
y the price of the i-th wine will be y*pi, i.e. y-times more than the current
year.

You want to sell all the wines you have, but you want to sell exactly one wine
per year, starting on this year. One more constraint - on each year you are
allowed to sell only either the leftmost or the rightmost wine on the shelf and
you are not allowed to reorder the wines on the shelf (i.e. they must stay in
the same order as they are in the beginning).

GOAL:
You want to find out, what is the maximum profit you can get, if you sell
the wines in optimal order.

EXAMPLE:
So for example, if the prices of the wines are (in the order as they are placed
on the shelf, from left to right): p1=1, p2=4, p3=2, p4=3 The optimal solution
would be to sell the wines in the order p1, p4, p3, p2 for a total profit 1*1 +
3*2 + 2*3 + 4*4 = 29


## Write a backtrack
Here are some restrictions I put on a backtrack solution:

1. it should be a function, calculating the answer using recursion
2. it should return the answer with return statement, i.e. not store it somewhere
3. all the non-local variables that the function uses should be used as read-only,
i.e. the function can modify only local variables and its arguments.

"""
def memoize(f):
    cache = {}
    def memoizedFunction(*n):
      if n not in cache:
         cache[n] = f(*n)
      return cache[n]
    return memoizedFunction


@memoize
def checkio(l,y=0):
    y=y+1
    if not l:
        return 0
    else:
        return max(y*l[0]+ checkio(l[1:],y), y*l[-1] + checkio(l[:-1],y))




print checkio((2,3,5,1,4,6,6,6,6,6,5,8,7,9,6,54,7,8,5,12,36,6,89,78,66))
