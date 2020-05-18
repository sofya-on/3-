from gorner import gorner
from top import mmax
from derivation import derivative
from functools import partial
from secant_method import secant_method, sign

def newtone(p):
    eps = 0.00001
    s = sign(p[0])
    p = list(map(lambda x: s * x, p))
    b = mmax(p)
    a = b
    s1 = sign(gorner(p, b))
    s2 = s1
    gornerP = partial(gorner, p)
    gornerDer = partial(gorner, derivative(p))
    while s1 == s2:
        a -= 0.5
        s2 = sign(gornerP(a))
    x = (a + b) / 2.
    while abs(gornerP(x) / gornerDer(x)) >= eps:
        x -= gornerP(x) / gornerDer(x)
    return x

if __name__ == "__main__":
    p = [-7, 4, 8]
    print(newtone(p))
    print(secant_method(p))
