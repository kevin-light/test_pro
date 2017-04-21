d={'a':1,'b':2,'c':3}
for key in d:
  print(key)

for value in d.values():
  print(value)
for k,v in d.items():
  print(k,v)

for ch in 'qwe':
  print(ch)

  #如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance('123',Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
  print(i,value)

for x,y in [(1,2),(2,1)]:
  print(x,y)