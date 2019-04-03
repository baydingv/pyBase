# -*- coding: utf-8 -*-
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
# -----------------------------------------------------------------------
entity = {}
N = int(input('введи количество предприятий: '))
for i in range(N):
    nm = input('введи имя: ')
    P1 = int(input('прибыль за 1й квартал: '))
    P2 = int(input('прибыль за 2й квартал: '))
    P3 = int(input('прибыль за 3й квартал: '))
    P4 = int(input('прибыль за 4й квартал: '))
    entity[nm] = [P1,P2,P3,P4]

summ,tot = 0,0
for en in entity:
    rec = entity.get(en)
    summ += sum(rec)
    tot  += len(rec)
mean = summ/(tot*1.0)

lst_abv,lst_und = [],[]
for en in entity:
    rec = entity.get(en)
    mean_i = 1.0*sum(rec)/len(rec)
    if mean_i > mean: lst_abv.append(en)
    else:             lst_und.append(en)
    
print('\nсредняя прибыль %f: '%(mean))
print('прибыль выше средней у: ')
print(lst_abv)
print('прибыль ниже средней у: ')
print(lst_und)

