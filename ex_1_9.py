# -*- coding: utf-8 -*-
LLL = input('введи три числа: ')
s = LLL.split()
L1,L2,L3 = float(s[0]),float(s[1]),float(s[2])

if(L2<L1):
    L1,L2 = L2,L1
if(L3<L2):
    L2,L3 = L3,L2 
if(L2<L1):
    L1,L2 = L2,L1
    
print('средним оказалось число: {}'.format(L2))

 