#-*- coding:utf-8 -*-
std1={'name':'michael','score':98}
std2={'name':'bob','score':88}
def print_score(std):
  print('%s: %s' % (std['name'],std['score']))
print(std1)

class Student(object):
  def __init__(self,name,score):
    self.name=name
    self.score=score
  def print_score(self):
    print('%s : %s' % (self.name,self.score))

bart=Student('Bart Simpson',59)
lisa=Student('Lisa impson',87)

bart.print_score()
lisa.print_score()

class myclass(object):
  i=123
  def __init__(self):
    self.i=345
a=myclass()
print(a.i)
print(myclass.i)