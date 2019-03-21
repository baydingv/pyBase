# -*- coding: utf-8 -*-
d_chr = input('введи номер буквы в алфавите: ')
n = int(d_chr)
if (n>26):
    print('стольких букв нет в английском алфавите!!')
else:
    print('это - буква {}'.format(chr(n + ord('a') - 1)))

 