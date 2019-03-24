# -*- coding: utf-8 -*-
#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
def sumfig(num):
    if num==0: return 0;
    return sumfig(num//10) + (num % 10)


lst=[]
while 1:
    next = int(input('введи натуральное число, или 0 - конец набора: '))
    if next== 0: break;
    lst.append(next)

sum_record =0; recordsmen =0
for i in lst: 
    sum_i = sumfig(i)
    if sum_i > sum_record:
        sum_record,recordsmen =sum_i,i

print('{} {}'.format(recordsmen,sum_record))