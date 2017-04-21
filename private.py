#-*- coding:utf-8 -*-
class Student(object):
  def __init__(self,name,score):
    self.__name=name
    self.__score=score
  def print_score(self):
    print('%s:%s' % (self.__name,self.__score))


  def get_name(self):
    return self.__name
  def set_score(self,score):
    return self.score
  def set_score(self,score):
    if 0<=score<=100:
      self.__score=score
    else:
      raise ValueError('bas score')
bart = Student('Bart simposn',98)
print(bart.get_name())

bart.__name='new name'
print(bart.__name)
print(bart.get_name())
