#-*- coding:utf-8 -*-
print(type(abs))
print(type(123)==type(456))

import types
def fn():
  pass
print(type(fn)==types.FunctionType)

print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
  def __len__(self):
    return 100
dog=MyDog()
print(len(dog))
print('ABC'.lower())

class MyObject(object):
  def __init__(self):
    self.x=9
  def power(self):
    return self.x*self.x
obj=MyObject()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(obj.y)
print(getattr(obj,'y'))
print(getattr(obj,'z',404))

print(hasattr(obj,'power'))
fn=getattr(obj,'power')
print(fn())

def readImage(fp):
  if hasattr(fp,'read'):
    return readData(fp)
  return None