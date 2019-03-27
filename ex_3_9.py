# -*- coding: utf-8 -*-
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
N = 10
minimal = [10000]*N
A = [[ random.randint(-100,100) for _ in range(N)] for _ in range(N)]
for i in range(N):
    s = ''
    for j in range(N):
        s = s + '{0:4} '.format(A[i][j])
        if A[i][j] < minimal[j]: minimal[j] = A[i][j]
    print(s)
print('max(min) = {}'.format(max(minimal)))