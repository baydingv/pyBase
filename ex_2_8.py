# -*- coding: utf-8 -*-
#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности
# чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, 
# задаются вводом с клавиатуры.
import random
def get_cnt(n,i):
    #input(n)
    if n==0: return 0
    rmd = n % 10
    iRet = get_cnt(n//10,i)
    if rmd==i: iRet += 1
    return iRet    
                
n = int(input('Введи количество чисел (сами числа будут генериться рандомно):'))
f = int(input('Введи конкретную цифру:'))

lst=[]
for i in range(n):
    lst.append(random.randint(0,1000000000))
cnt = 0
for en in lst:
    cnt += get_cnt(en,f)
    
print(lst)    
print(cnt)