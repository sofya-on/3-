def mmax(p):
    a = 0
    flag = 1
    while (flag == 1):
        sum = 0
        a += 1
        flag = 0
        if p[0] <= 0:
            flag = 1
        for i in range(0, len(p)):
            sum *= a
            sum += p[i]
            if sum < 0:
                flag = 1
    return a

if __name__ == "__main__":
    p = [-7, 4, 8]
    print(my_top(p))


        
