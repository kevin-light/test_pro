#-*- coding:utf-8 -*-
#sorted 排序
print(sorted([125,2,-6,0]))
print(sorted([125,2,-6,0],key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
  return t[0].lower()
def by_score(t):
  return t[1]
print(sorted(L,key=by_name))
print(sorted(L,key=by_score,reverse=True))

print('{:>8}'.format('189'))