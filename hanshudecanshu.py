#-*- coding:utf-8 -*-
def power(x,n=2):      #n=2 必选参数在前，默认参数在后
  s=1
  while n>0:
    n=n-1
    s=s*x
  return s
print (power(5,3))
print(power(5))

def enroll(name,gender,age=6,city='shanghai'):
  print('name:',name)
  print('gender:',gender)
  print('age:',age)
  print('city:',city)
print(enroll('sarah','F',None,'bj'))

#默认参数
def add_end(L=None):
  if L is None:
    L=[]
  L.append('END')
  return L
print(add_end([1,2,3]))
print(add_end())
print(add_end())

#可变参数
def calc(*numbers):
  sum = 0
  for n in numbers:
    sum=sum+n*n
  return sum
print(calc())
nums=[1,2,3]
print(calc(*nums))

#关键字参数函数
def person(name,age,**kw):
  print('name:',name,'age:',age,'other:',kw)
print(person('michael',11))
print(person('bob',12,city='shanghai'))
print(person('bob',12,city='shanghai',job='IT'))
extra={'city':'beijing','job':'engineer'}
print(person('jicj',22,**extra))

def person(name,age,**kw):
  if 'city' in kw:
    pass
  if 'job' in kw:
    pass
  print('name:',name,'age:',age,'other:',kw)
print(person('jack',23,city='biji',addr='chaoyang',job='jdjd'))

def person(name,age,*,city,job):
  print(name,age,city,job)
print(person('jck',23,city='bj',job='it'))

def person(name,age,*,city='beijing',job):
  print(name,age,city,job)
print(person('jck',23,job='jdsk'))

#参数组合顺序  必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kw):
  print('a:',a,'b:',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
  print('a:',a,'b:',b,'c=',c,'d=',d,'kw=',kw)
print(f1(1,2))
print(f1(1,2,3,'a','b'))
print(f1(1,2,3,x=9))
print(f2(1,2,3,d=3,ext=None))