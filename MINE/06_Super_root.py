# import math
# ERR = 0.0000000000001


# def LambertW_Newton(x):
#     w = x
#     while True:
#         eW = math.exp(w)
#         wNew = w - (w * eW - x) / (w * eW + eW)
#         if abs(w - wNew) <= ERR:
#             break
#         w = wNew
#     return w


# def super_root(n):
#     def m(n):
#         n = round(n, 15)
#         return int(n) if n == int(n) else n
#     return m(math.exp(LambertW_Newton(math.log(n))))

# print super_root(9999999999)
import os.path
def Name(**kw):
    assert len(kw)==1
    name, obj = kw.items()[0]
    obj.func_name = name
    return obj

def main():
    f = Name(CheckExists=lambda x:os.path.exists(x))
    print f()

main()
