# -*- coding: utf-8 -*-
#задание 3.2: Во втором массиве сохранить индексы четных элементов первого массива...
# исходный вариант. Посчитаем размер используемых переменных
import random
from pympler import asizeof
N = 100
ar1,ar2 = [],[]

for i in range(N): 
    k = random.randint(1,100)
    ar1.append(str(k))
    if k%2 == 0: ar2.append(str(i))
    
print(ar1)     
print(ar2)     
print('total arrays size= %d'%(asizeof.asizeof(ar1)+asizeof.asizeof(ar2)))
print()
print()

# теперь массивы превратим в строки: информация осталась, а памяти требуется на порядок меньше!
ar1 = ','.join(ar1)
ar2 = ','.join(ar2)
print(ar1)     
print(ar2)     
print('total arrays size= %d'%(asizeof.asizeof(ar1)+asizeof.asizeof(ar2)))

