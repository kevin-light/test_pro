#-*- coding:utf-8 -*-
#filter()也接收一个函数和一个序列,返回值是True还是False决定保留还是丢弃该元素

def is_old(n):
  return n%2==1
print(list(filter(is_old,[1,2,3,4,5,6,7,8,9])))

def not_empty(s):
  return s and s.strip()
print(list(filter(not_empty,['A',None,'',' '])))

#筛选素数

def _odd_iter():
  n=1
  while True:
    n=n+2
    yield n
def _not_divisible(n):
  return lambda x:x%n>0
def primes():
  yield 2
  it = _odd_iter()
  while True:
    n=next(it)
    yield n
    it = filter(_not_divisible(n),it)
for n in primes():
  if n <100:
    print(n)
  else:
    break


def is_palindrome(n):
  if str(n)==str(n)[::-1]   #[x::y,],x表示从x开始，y表示走y步取一个值，依次到取完为止,比如2是指每2个截取一个. -1指从倒数开始截取
    return True
  else:
    return False

output=filter(is_palindrome,range(1,100))
print(list(output))