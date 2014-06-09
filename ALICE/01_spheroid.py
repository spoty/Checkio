from math import pi, sqrt, asin, atanh

def spehroid(h,w):
    r=0.5*w
    return round(4*pi*r**2,2)

def prolate_spheroid(h,w):
    a,c = w*0.5, h*0.5
    e2 = 1-(a**2/c**2)
    e = sqrt(e2)
    return round(2*pi*a**2*(1+c/(a*e)*asin(e)),2)

def oblate_spheroid(h,w):
    a,c = w*0.5, h*0.5
    e2 = 1-(c**2/a**2)
    e = sqrt(e2)
    surface=round(2*pi*a**2*(1+(1-e2)/e*atanh(e)),2)
    return surface

switch = {
    1: prolate_spheroid,
    2: oblate_spheroid,
    3: spehroid
}

def checkio(h,w):
    return [round(((4/3)*pi*(w*0.5)**2*h*0.5),2), switch[1 if h>w else 2 if h<w else 3](h,w)]

print checkio(4,2)
