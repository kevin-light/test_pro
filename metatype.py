class Hello(object):
  def hello(self,name='world'):
    print('Hello,%s.' % name)
h=Hello()
print(h.hello())
print(type(Hello))
print(type(h))

#metaclass是类的模板，所以必须从‘type’派生
class ListMetaclass(type):
  def __new__(cls,name,bases,attrs):
    attrs['add']=lambda self, value: self.append(value)
    return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
  pass

#ORM(Object Relational Mapping)框架
class User()