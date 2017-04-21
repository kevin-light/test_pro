#-*- coding:utf-8 -*-  
#偏函数 Partial_function
print(int('12345',base=8))
print(int('12345',8))

def int2(x,base=2):
  return int(x,base)
print(int2('100000'))

import functools
int2=functools.partial(int,base=2)
print(int2('1010101'))
#int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值
print(int2('122099',base=10))