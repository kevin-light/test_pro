#-*- coding:utf-8 -*-
def log(func):
  def wrapper(*args,**kw):
    print('call %s():' % func.__name__)
    return func(*args,**kw)
  return wrapper
@log
def now():
  print('20170223')
print(now())

def log(text):
  def decotator(func):
    def wrapper(*args,**kw):
      print('%s %s():' % (text,func.__name__))
      return func(*args,**kw)
    return wrapper
  return decotator
@log('execute')
def now():
  print('170223')
print(now())
print(log('execute')(now))
print(now.__name__)


import functools
def log(func):
  @functools.wraps(func)
  def wrapper(*args,**kw):
    print('call %s():' % func.__name__)
    return func(*args,**kw)
  return wrapper
  #者针对带参数的decorator
import functools
def log(text):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
      print('%s %s():' % (text,func.__name__))
      return func(*args,**kw)
    return wrapper
  return decorator

#作业
import functools
def wrapper(text,func):
  @functools.wraps(func)
  def wrapper(*args,**kw):
    print('%s %s():' % (text,func.__name__))
    return [func(*args,**kw),print('%s %s():' (text,func.__name__))][0]
  return wrapper

def log(arg):
  text='execute'
  if isinstance(arg,str):
    text=arg
    def decorator(func):
      return weapper(text,func)
    return decorator
  else:
    func=arg
    return wrapper(text,func)
@log
def now():
  print('2017-02-23')
print(now)