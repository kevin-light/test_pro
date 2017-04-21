#-*- coding:utf-8 -*-
class Student(object):
  pass
#给实例绑定属性
s=Student()
s.name = 'mic'
print(s.name)

#给实例绑定一个方法
def set_age(self,age):
  self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)
#gei所有属性绑定方法
def set_score(self,score):
  self.score = score
Student.set_score=set_score
s.set_score(99)
print(s.score)

class Studnet(object):
  __slots__=('name','age')
s=Student()
s.name='mic'
s.age=27
s.score=90
