#-*- coding:utf-8 -*-
class Animal(object):
  def run(self):
    print('Animal is runing...')
class Dog(Animal):
  pass
class Cat(Animal):
  pass
dog=Dog()
print(dog.run())
cat=Dog()
cat.run()

class Dog(Animal):
  def run(self):
    print('dog is run')
class Cat(Animal):
  def run(self):
    print('cat is run')
dog=Dog()
print(dog.run())
cat=Cat()
cat.run()

a=list()
b=Animal()
c=Dog()
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(b,Dog))

def run_twic(animal):
  animal.run()
  animal.run()
run_twic(Dog())

class Tortoise(Animal):
  def run(self):
    print('Tortoise is run')
print(run_twic(Tortoise()))

class Timer(object):
  def run(self):
    print('Start..')