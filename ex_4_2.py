# -*- coding: utf-8 -*-
#2. Написать два алгоритма нахождения i-го по счёту простого числа.
# ● Без использования Решета Эратосфена;
# ● Использовать алгоритм решето Эратосфена
# -----------------------------------------------------------------------
import profile
def simple(n):
    Res = [2]
    cnt,k = 1,1
    while cnt < n:
        k += 2
        C = False
        for en in Res:
            if C: break
            if k % en == 0:  C = True
        if not C: Res.append(k); cnt += 1
    return Res[-1:]
        
# -----------------------------------------------------------------------
# n = 100  r=    541   t1(erato)=0.328    t2(simple)=0.000
#     200       1223             0.359               0.000
#     400       2741             0.391               0.016 
#     800       6133             0.406               0.094            
#    1600      13499             0.438               0.312                
#    3200      29443             0.484               1.234 
#    6400      63809             0.500               4.656 
#   12800     137477             0.547              18.672             
#   25600     294809             0.625              75.078 
#                             O(ln(N))              O(N^2)                      
# -----------------------------------------------------------------------
def erato(n):
    M = 1000001
    A = [True]*M  
    A[0],A[1],succs = False,False,True
    cnt,ind = 0,0
    while cnt < n:
        while not A[ind] and ind < M-2: ind += 1
        if ind > M - 2: succs = False; break
        cnt += 1
        
        for i in range(ind,M,ind): A[i] = False
        ind += 1
    if succs: return ind-1
    else:     return 0
      
    
def main():
    N = 1600
#    erato(N)
#    simple(N)
    print('по счету {}-е простое = {}'.format(N,erato(N)))
    print('по счету {}-е простое = {}'.format(N,simple(N)))
    
profile.run('main()')