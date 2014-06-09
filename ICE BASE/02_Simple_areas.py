import math
def simple_areas(*args):
    if len(args) ==  3: p = ((args[0]+args[1]+args[2])*0.5)
    return round(math.pi*(args[0]*0.5)**2,2) if len(args) == 1 else round(args[0]*args[1],2) if len(args) == 2 else round(math.sqrt(p*(p-args[0])*(p-args[1])*(p-args[2])),2) if len(args) == 3 else 0
# ( ((a+b+c) * (a+b-c) * (a+c-b) * (b+c-a)) ** 0.5 ) / 4
print simple_areas(3)
