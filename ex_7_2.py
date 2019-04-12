# -*- coding: utf-8 -*-
#задание 7.2: Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

# слияние двух отсортированных списков в один 
def sli(A,B):
    R=[]
    i1,i2,N1,N2 = 0,0,len(A),len(B)
    while i1<N1 or i2<N2:
        if i1==N1:
            for i in range(i2,N2): R.append(B[i])
            break
        if i2==N2:
            for i in range(i1,N1): R.append(A[i])
            break
        if A[i1]<B[i2]:  R.append(A[i1]); i1 += 1
        else:            R.append(B[i2]); i2 += 1
    return R

import random
N = 16
A = [random.uniform(0,50.0) for _ in range(N)]
print('исходный массив')
print(A)   

R = []
for i in range(N):   R.append([A[i]])

while len(R)>1:
    for i in range(0,len(R),2):     R[i] = sli(R[i],R[i+1])
    for i in range(len(R)-1,0,-2):  R[i:i+1] = []  

print('\n итоговый результат')
print(R[0])   
