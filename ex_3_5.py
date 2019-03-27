# -*- coding: utf-8 -*-
#5. В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.

s = (input('введи строку чисел: ')).split()
a = [int(en) for en in s]
max_v,ind = -10000,-1
for i,en in enumerate(a):
  if en < 0:
    if en > max_v: max_v,ind = en,i

print(max_v, ind)