# -*- coding: utf-8 -*-
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import profile
import random

def prep(N):
  return [[ random.randint(-100,100) for _ in range(N)] for _ in range(N)]
  
def prog(A,N):
  minm = [1000]*N
  for i in range(N):
    for j in range(N):
      if minm[j] > A[i][j]: minm[j] = A[i][j]
  return max(minm)

def prog_pro(A,N):
    maxmin = -1000
    for j in range(N):
        min_in_column = 1000
        for i in range(N):
            if min_in_column > A[i][j]: min_in_column = A[i][j]
            if min_in_column < maxmin:  break
 
        if min_in_column > maxmin:  maxmin = min_in_column
    return maxmin
# ---------------------------------------------------------------------  
# N =353  t_prep= 6,656   t_prog=0,031  t_prog_pro=0,016
#    500         13,500          0.062             0.016                
#    707         25.047          0.141             0.047                  
#   1000         51.828          0.281             0.078                 
#   1414        110,266          0,688             0,438                        
#   2000        209,516          1,266             2,016                                            
# ---------------------------------------------------------------------  
#                 O(N^2)         O(N^2)       сильно нерегулярно
#
        
def main():
  N = 353
  A = prep(N)
  print(prog(A,N))
  print(prog_pro(A,N))
  
profile.run('main()')