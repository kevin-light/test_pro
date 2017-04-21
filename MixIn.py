#-*- coding:utf-8 -*-
class Animal(object):
  pass
class Mammal(Animal):
  pass
class Bird(Animal):
  pass
class Dog(mammal):
  pass
class bat(Mammal):
  pass
class Parrot(Bird):
  pass
class Parrot(Bird):
  pass
class Ostrich(Bird):
  pass

class Runnable(object):
  def run(self):
    print('Runnable...')
class Flyable(object):
  def fly(slef):
    print('flying')
class Dog(Mammal,Runnable):
  pass
class Bat(Mammal,Flyable):
  pass
class Dog(Mammal,runnaleMixIn,carnivorousMixIn):
  pass
#编写多线程的TCP,UDP服务
class MyTCPServer(TCPServer,ForkingMixIn):
  pass
class MyUPDServer(UDPServer,ForkingMixIn):
  pass

classMyTCPServer(TCPServer,CoroutineMixIn):
pass