# -*- coding: utf-8 -*-
#1 Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, 
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' 
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), 
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

while 1:
    strn = input('введи операцию вида: a op b, разделяя слова пробелом: ')
    lst = strn.split(' ')
    a = float(lst[0]) 
    b = float(lst[2])
    op = lst[1]

    if op == '0': break
    elif op == '+': res = a + b
    elif op == '-': res = a - b
    elif op == '*': res = a * b
    elif op == '/': 
        if b==0: print('делить на ноль неэтично...'); continue
        else:    res = a / b
    else: print('операция {} не поддерживается...'.format(op)); continue
    print('{} = {}'.format(strn,res))