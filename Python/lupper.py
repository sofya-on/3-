def lupper(arr):
    max_neg = -1
    for i in range(len(arr)):
        if (arr[i] < 0) and (abs(arr[i]) > max_neg):
            max_neg = abs(arr[i])

    for i in range(len(arr)):
        if arr[i] < 0:
            first_neg_ind = i
            break

    u_border = 1 + pow(max_neg / arr[0], 1 / first_neg_ind)
    return u_border


n = int(input('Введите длину полинома: '))
arr = [float(input()) for i in range(n)]
print(lupper(arr))
