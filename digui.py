#-*- coding:UTF-8 -*-
#递归函数：一个函数在内部调用自身本身。

def fact(n):
  if n==1:
    return 1
  return n*fact(n-1)
print(fact(10))

def fact(n):
  return fact_iter(n,1)
def fact_iter(num,product):
  if num == 1:
    return product
  return fact_iter(num-1,num*product)
print(fact(10))

#移动汉诺塔

def move(n,a,b,c):
  if n==1:
    print('move',a,'-->',c)
    return
  move(n-1,a,c,b)
  print('move',a,'-->',c)
  move(n-1,b,a,c)
move(4,'A','B','C')


L=[]
n=1
while n<=99:
  L.append(n)
  n=n+2