def gorner(p, a):
    sum = 0
    for i in range(len(p)):
        sum *= a
        sum += p[i]
    return sum

if __name__ == "__main__":
    p = [-5, -1, 3, -2, 5]
    a = -1
    print(gorner(p, a))