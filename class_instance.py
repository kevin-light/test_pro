#-*- coding:utf-8 -*-
# class Student(object):
#   pass
# bart = Student()
# print(bart)
# print(Student)

# class Student(object):
#   def __init__(self,name,score):
#     self.name=name
#     self.score=score
# bart = Student('Bart Simpson',59)
# print(bart.name)
# print(bart.score)

# def print_score(std):
#   print('%s:%s' % (std.name,std.score))
# print_score(bart)

class Student(object):
  def __init__(self,name,score):
    self.name=name
    self.score=score
  def print_score(self):
    print('%s: %s' % (self.name,self.score))
bart = Student('Bart Simpson', 59)
bart.print_score()

class Student(object):
  def __init__(self,name,score):
    self.name=name
    self.score=score
  def print_score(self):
    print('%s: %s' % (self.name,self.score))
bart = Student('Bart Simpson', 59)
bart.print_score()

  def get_grade(self):
    if self.score>=90:
      return 'A'
    elif self.score>=60:
      return 'B'
    else:
      return 'C'

bart.get_grade()
