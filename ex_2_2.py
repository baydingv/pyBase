# -*- coding: utf-8 -*-
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).   

n = int(input('введи n: '))
odd,even=0,0
while n>0:
    ni = n%10
    if ni%2 == 0: even += 1
    else:          odd += 1
    n = n//10
print('нечетных {}, а четных {}'.format(odd,even))