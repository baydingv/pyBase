# -*- coding: utf-8 -*-
#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. 
#Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
import random
def sum_fig(n,i):
    k = 0
    if n>0: k = sum_fig(n//10,i)
    if n%10 == i: k += 1
    return k 

n = int(input('введи n -количество чисел в последовательности: '))
fig = int(input('введи i -искомую цифру: '))
lst,sum=[],0
for i in range(n):
    a = random.randint(0,1000000000)
    sum += sum_fig(a,fig)
    lst.append(a)

print(lst)
print('цифр {} всего {} штук'.format(fig,sum))