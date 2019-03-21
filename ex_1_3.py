# -*- coding: utf-8 -*-
xy1 = input('введи      x y: ')
s = xy1.split()
x1,y1 = float(s[0]),float(s[1])

xy2 = input('введи еще x y: ')
s = xy2.split()
x2,y2 = float(s[0]),float(s[1])

k = (y2-y1)/(x2-x1)
b = y1 - k*x1
print('y = k*x + b  : k={}, b={}'.format(k,b))