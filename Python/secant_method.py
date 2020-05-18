from top import mmax
from gorner import gorner
from functools import partial

def sign(x):
    return 1. if x >= 0 else -1

def secant_method(p):
    eps = 0.001
    s = sign(p[0])
    p1 = list(map(lambda x: s * x, p))
    gornerP = partial(gorner, p1)
    b = mmax(p1)
    a = b
    s1 = sign(gornerP(b))
    s2 = s1
    while s1 == s2:
        a -= 0.5
        s2 = sign(gornerP(a))
    while(abs(b - a) > eps and (a != b)):
        a = b - (b - a) * gornerP(b) / (gornerP(b) - gornerP(a))
        if a != b:
            b = a + (a - b) * gornerP(a) / (gornerP(a) - gornerP(b))
    return b

if __name__ == "__main__":
    p = [-7., 4., 8.]
    print(secant_method(p))
