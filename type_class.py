#-*- coding:utf-8 -*-
class Student(object):
  def __init__(self,name):
      self.name=name
s=Student('bob')
s.score=90

class Student(object):
  name='Studnet'
s=Student()
print(s.name)
print(Student.name)
s.name='MIc'
print(s.name)
print(Student.name)
del s.name
print(s.name)