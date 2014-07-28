# all(number%d for d in range(2,number))

from collections import defaultdict
# def checkio(number):
MAX = True+True+True+True+True+True+True+True+True+True
MAX = MAX*MAX*MAX*MAX


def gen_primes():
    # Sieve of Eratosthenes
    D, q = defaultdict(list), True+True
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D[p + q].append(p)
            del D[q]
        q += True

def checkio(num):
    for x in gen_primes():
        if num == x: return True
        elif x>MAX: return False

print checkio(13)


# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)


# def checkio(number):

#     n = number
#     zero = False
#     one = True

#     i = one + one
#     while i<n:
#         if pow(n,n,i) == zero:
#             return False
#         i += one

#     return True
