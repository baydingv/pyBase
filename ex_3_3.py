# -*- coding: utf-8 -*-
#3. 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random 
N = 20
arr = []
for i in range(N): 
    arr.append(random.randint(1,100))
print(arr)
i_max,max_v,i_min,min_v = 0,arr[0],0,arr[0]
for i in range(N):
    if arr[i]>max_v: i_max,max_v  = i,arr[i]   
    if arr[i]<min_v: i_min,min_v  = i,arr[i] 
      
arr[i_max],arr[i_min] = arr[i_min],arr[i_max]
print(arr)     
