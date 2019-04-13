# -*- coding: utf-8 -*-
# задание 8.1. Определить количество различных подстрок с использованием 
# хеш-функции. Задача: на вход функции дана строка, требуется вернуть 
# количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib

# Провести поиск подстроки в строке, начиная с позиции j
def rabin_karp(s, t, j):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(j, len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            return i
    return -1

the_string = 'little cat sitting on a tree'
cnt,cnt_d = 0,0
LT = len(the_string)
for Li in range(1,LT):
  for ib in range(0,LT-Li):
    t = the_string[ib:ib+Li]
    cnt += 1
    if rabin_karp(the_string, t, ib+1)==-1:
        cnt_d += 1
#    else:
#        print(t)

print('from %d subs %d are distinqt'%(cnt,cnt_d))
