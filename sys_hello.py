#-*- coding:utf-8 -*-


'atest module'

__author__='Michael Liao'

import sys
def test():
  args=sys.argv
  if len(args)==1:
    print('hello,world')
  elif len(args)==2:
    print('hello,%s?' % args[1])
  else:
    print('tpp many arguments!')
if __name__=='__main__':   #http://www.jb51.net/article/51892.htm
  test()

#private函数
def _private_1(name):
  return 'hello,%s'% name
def _private_2(name):
  return 'hel, %s' % name
def greeting(name):
  if len(name)>3:
    return _private_1(name)
  else:
    return _private_2(name)