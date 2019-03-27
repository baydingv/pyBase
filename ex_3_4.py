# -*- coding: utf-8 -*-
#4. Определить, какое число в массиве встречается чаще всего
import random 
a = [random.randint(0,10) for en in range(50)]
print(a)
num,cnt=[],[]
while len(a)>0:
    num_i = a[0]
    num.append(num_i)
    cnt.append(0)
    while num_i in a:
        a.remove(num_i)
        cnt[len(cnt)-1] += 1

#print(num)
#print(cnt)
max_v = max(cnt)
i_max = cnt.index(max_v)
print('самое частое число: {}'.format(num[i_max]))