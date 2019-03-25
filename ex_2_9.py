# -*- coding: utf-8 -*-
#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
#Вывести на экран это число и сумму его цифр.
def sum_fig(n):
    k = 0
    if n>0: k = sum_fig(n//10)
    return( k + n%10)
        
st = input('введи ряд натуральных чисел через пробел: ')
lst = st.split(' ')
rec,recman = 0,0
for en in lst:
    im =int(en)
    sum_i = sum_fig(im)
    if sum_i>rec: rec,recman = sum_i,im
print('{}  {}'.format(rec,recman)) 