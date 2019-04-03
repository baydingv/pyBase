# -*- coding: utf-8 -*-
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как 
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# -----------------------------------------------------------------------
dig = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
fig = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

stri = input('введи: А1 оп А2, где аргументы А1,А2 имеют 16ричный вид: ')
s = stri.split(' ')
A1,A2,op = s[0],s[2],s[1]
L1,L2 = len(A1),len(A2)
D1,D2 = 0,0

#print('%s %d'%(A1,L1))
#print('%s %d'%(A2,L2))
#print('%s '%(op))

for i in range(L1):
    D1 = D1 + 16**i * dig.get(A1[L1 -1 - i])
for i in range(L2):
    D2 = D2 + 16**i * dig.get(A2[L2 -1 - i])

#print('%d %d'%(D1,D2))
if   op == '+':
    D = D1 + D2
elif op == '*':
    D = D1 * D2
else: print('unknown operation'); exit(0)

H=''
#print('%s = %d'%(stri, D))
while D > 0:
    Hi = D % 16
    D //= 16
    H = "".join([fig.get(Hi), H])
print(str(H))
