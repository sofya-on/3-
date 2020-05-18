def ring(array):
    if array[0] == 0: array[0] = array[1]

    if array[len(array) - 1] == 0: array[len(array) - 1] = arr[len(array) - 2]

    max = abs(array[1])
    for i in range(2, len(array)):
        if abs(array[i]) > max:
            max = abs(array[i])
        else: continue
    upper = 1 + max / abs(array[0])
    max = abs(array[0])
    for i in range(1, len(array) - 1):
        if abs(array[i]) > max:
            max = abs(array[i])
        else: continue

    bottom = 1 / (1 + max / abs(array[len(array) - 1]))
    return bottom, upper

a = int(input('Длина полинома: '))
array = [int(input()) for i in range(a)]

print('Нижняя и верхняя границы кольца:', ring(array))
