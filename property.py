#-*- coding:utf-8 -*-
class Student(object):
  @property
  def score(self):
    return self.score
  @score.setter
  def score(self,value):
    if not isinstance(value,int):
      raise ValueError('score must be an integer')
    if value <0 or value > 100:
      raise ValueError('score muset between 0-100')
    self._score=value

class Student(object):
  @property
  def birth(self):
    return self._birth
  @birth.setter
  def birth(self,value):
    self._birth=value
  @property
  def age(self):
    return 2015 - self._birth

class Screen(object):
  @property
  def width(self):
    return self._width
  @width.setter
  def width(self,width):
    self._width=width
  @property
  def height(self):
    return self._height
  @height.setter
  def height(self,height):
    self._height=height
  @property
  def resolution(self):
    return self._height*self._width
s=Screen()
s.width=1024
s.height=768
print(s.resolution)