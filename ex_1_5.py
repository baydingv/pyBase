# -*- coding: utf-8 -*-
d_chr = input('введи две буквы    cL,cR: ')
s = d_chr.split(); cL = ord(s[0][0].lower()); cR = ord(s[1][0].lower())
print('симмвол {} стоит на {}-м месте алфавита'.format(chr(cL),cL-ord('a')+1))
print('симмвол {} стоит на {}-м месте алфавита'.format(chr(cR),cR-ord('a')+1))
print('между ними ещё {} букв'.format(abs(cR-cL-1)))
 