def derivative(p):
    def worker():
        newp = p[:-1]
        l = len(newp)
        for i in range(l):
            newp[i] *= abs(l - i)
        return newp
    return worker() if len(p) != 1 else 0

if __name__ == "__main__":
    p = [1,2,3,4,5]
    print(derivative(p))