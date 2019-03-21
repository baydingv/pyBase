# -*- coding: utf-8 -*-
LLL = input('введи длины трех отрезков L1,L2,L3: ')
s = LLL.split()
L1,L2,L3 = float(s[0]),float(s[1]),float(s[2])

if(L2<L1):
    L1,L2 = L2,L1
if(L3<L2):
    L2,L3 = L3,L2 
if(L2<L1):
    L1,L2 = L2,L1
if( L3>L2+L1):
    print('такого треугольника не существует')
else:
    if(L3==L2 and L1==L2):
        print('треугольник равносторонний')
    elif(L3!=L2 and L1!=L2 and L1!=L3):
        print('треугольник разносторонний')
    else:
        print('треугольник равнобедренныий')
        
        