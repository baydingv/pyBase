# -*- coding: utf-8 -*-
import random
d_int = input('введи целочисленный диапазон nL,nR: ')
d_flt = input('введи float диапазон         xL,xR: ')
d_chr = input('введи диапазон char          cL,cR: ')
s = d_int.split(); nL = int(s[0]);   nR = int(s[1])
s = d_flt.split(); xL = float(s[0]); xR = float(s[1])
s = d_chr.split(); cL = ord(s[0][0]); cR = ord(s[1][0])
nC,xC,cC =  random.randint(nL,nR),random.random()*(xR-xL)+xL,chr(random.randint(cL,cR))
print('число  внутри диапазона: {} <= {} <= {}'.format(nL,nC,nR))
print('число  внутри диапазона: {} <= {} <= {}'.format(xL,xC,xR))
print('символ внутри диапазона: {} <= {} <= {}'.format(chr(cL),cC,chr(cR)))
