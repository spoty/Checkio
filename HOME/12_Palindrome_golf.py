golf=lambda l:[x for x in range(l+1,10**4)if`x`==`x`[::-1]*all(x%d for d in range(2,x))][0]
# golf=lambda l,r=range:next(x for x in r(10**6)if(x==int(`x`[::-1]))&all(x%d for d in r(2,x))and x>l)
golf=lambda l:next(x for x in range(l+1,98689)if`x`==`x`[::-1]*all(x%d for d in range(2,x)))
golf=lambda l:min(x for x in range(l+1,10**5)if`x`==`x`[::-1]*all(x%d for d in range(2,x)))


# 100
golf=lambda l,r=range:next(x for x in r(10**6)if(x==int(`x`[::-1]))&all(x%d for d in r(2,x))and x>l)

# 97
def golf(l):
    l+=1
    while ~-(`l`==`l`[::-1]*all(l%d for d in range(2,l))):l+=1
    return l

# # 103
def golf(l):
    l+=1
    while not(l==int(`l`[::-1]))&all(l%d!=0for d in range(2,l)):l+=1
    return l

# # 120
def golf(l):
    p=lambda n:(n==int(`n`[::-1]))&all(n%d!=0for d in range(2,n))
    while not(p(l+1)):l+=1
    return l+1

# # 123
def golf(l):
    p=lambda n:(str(n)==str(n)[::-1])&all(n%d!=0for d in range(2,n))
    while not(p(l+1)):l+=1
    return l+1

# # 124
def golf(l):
    p=lambda n:str(n)==str(n)[::-1]and all(n%d!=0for d in range(2,n))
    while not(p(l+1)):l+=1
    return l+1


golf=m=lambda l:l if(l==int(`l`[::-1]))&all(l%d for d in range(2,l))else m(l+1)




def golf(l):
    l+=l
    m=lambda l:l if(l==int(`l`[::-1]))&all(l%d for d in range(2,l))else m(l+1)


# (lambda f, n: f(f, n))(
# ...     lambda f, n: chr(n % 256) + f(f, n // 256) if n else "",
# ...     802616035175250124568770929992)


golf=lambda l:(lambda f,l:f(f,l+1))(lambda f,l:l if(l==int(`l`[::-1]))&all(l%d for d in range(2,l))else f(f,l+1),l)



n=lambda l,r=range:next(x for x in r(10**6)if(x==int(`x`[::-1]))&all(x%d for d in r(2,x))and x>l)


n=lambda l,r=range:min(x for x in r(l+1,10**4)if`x`==`x`[::-1]*all(x%d for d in r(2,x)))

# Why a lambda? Why a min of a filtered range? There may be a better way.

def golf(l):
    l+=1
    while not`l`==`l`[::-1]*all(l%d for d in range(2,l)):l+=1
    return l
print golf(5)
