import numpy as np

def division(_p1, _p2):
    p1 = np.array(_p1)
    p2 = np.array(_p2)
    dim = (len(p2), len(p1))
    newp = np.zeros(dim)
    newp[0, :] = p1
    (m, n) = dim
    d = p2[0]
    p2 = p2 * (-1)
    ost = np.zeros(m - 1)
    res = np.zeros(n - m + 1)
    len_res = len(res)
    for i in range(len_res):
        res[i] = np.sum(newp[:, i] / d)
        for k in range(1, m):
            newp[m - k, i + k] = res[i] * p2[k]
    for i in range(len_res, len(p1)):
        ost[i - len_res] = np.sum(newp[:, i])
    return (res, ost)

if __name__ == "__main__":
    p1 = [-1., -2., -2., -5., 0., -3., -4., 2., -5., 0.]
    p2 = [1., 4., 1., -14., -20., -8.]
    p3 = [1, 3]
    p4 = [1, 0, 0, -1]
    p5 = [1, 1, 1]
    print(division(p1, p2))
    print(division(p2, p3))
    print(division(p4, p5))
