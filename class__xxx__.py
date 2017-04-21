#-*- coding:utf-8 -*-
#定制类
class Student(object):
  def __init__(self,name):
    self.name=name
  def __str__(self):
    return 'Student object (name:%s)' % self.name
  __repr__=__str__
print(Student('Michael'))

class Fib(object):
  def __init__(self):
    self.a,self.b=0,1
  def __iter__(self):
    return self
  def __next__(self):
    self.a,self.b=self.b,self.a+self.b
    if self.a>100:
      raise StopIteration();
    return self.a
for n in Fib():
  print(n)

class Fib(object):
  def __getitem__(self,n):
    a,b = 1,1
    for x in range(n):
      a,b=b,a+b
    return a
f = Fib()
print('f[10]:',f[10])

class Fib(object):
  def __getitem__(self,n):
    if isinstance(n,int):
      a,b = 1,1
      for x in range(n):
        a,b = b,a+b
      return a
    if isinstance(n,slice):
      start = n.start
      stop = n.stop
      if start is None:
        start = 0
      a,b=1,1
      L = []
      for x in range(stop):
        if x >=start:
          L.append(a)
        a,b = b,a+b
      return L
f = Fib()
print(f[0:5])
print(f[:10:3])

class Student(object):
  def __init__(self):
    self.name='Mic'
  def __getattr__(self,attr):
    if attr=='score':
      return 99
s = Student()
print(s.name)
print(s.score)

class Student(object):
  def __getattr__(self,attr):
    if attr=='age':
      return lambda:25
#    raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s=Student()
print(s.age())
print(s.attr)

class Chain(object):
  def __init__(self,path=''):
    self._path = path
  def __getattr__(self,path):
    return Chain('%s/%s' % (self._path,path))
  def __str__(self):
    return self._path
  __repr__=__str__
print(Chain().status.user.timeline.list)

class Student(object):
  def __init__(self,name):
    self.name = name
  def __call__(self):
    print('My name is %s' % self.name)
s = Student('Mic')
print(s())

class Chain(object):
  def __init__(self,path='GET'):
    self._path = path
  def __getattr__(self,path):
    return Chain('%s/%s' % (self._path,path))
  def __call__(self,path):
    return Chain('%s/%s' % (self._path,path))
  def __str__(self):
    return self._path
  __repr__=__str__
print(Chain().users('michael').repos)

class FunctionalList:
  def __init__(self,values=None):
    if values is None:
      self.values=[]
    else:
      self.values=values
  def __len__(self):
    return len(self.values)
  def __getitm__(self,key):
    self.values[key]
  def __setitem__(self,key,value):
    self.values[key]=value
  def __delitem__(self,key):
    del self.values[key]
  def __iter__(self):
    return iter(self.values)
  def __reversed__(self):
    return reversed(self.values)
  def append(Self,value):
    self.values.append(value)
  def head(self):
    return self.values[0]
  def tail(self):
    return self.values[1:]
  def init(self):
    return self.values[:-1]

class Entity:
  def __init__(self,size,x,y):
    self.x,self.y=x,y
    self.size=size
  def __call__(self,x,y):
    self.x,self.y=y,x