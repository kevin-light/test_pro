#-*- coding:utf-8 -*-

L=list(range(1,11))
print(L)

L=[]
for x in range(1,11):
  L.append(x*x)
print(L)

[x*x for x in range(1,11)]
q=[m+n for m in 'abc' for n in '123']
print(q)


import os
print([d for d in os.listdir('.')])

d={'x':'a','c':'v','z':'D'}
for k,v in d.items():
  print(k,'=','v')
  print(k+'='+v)

L=['Hello','HJD','IBM']
print([s.lower() for s in L])