import os
print(os.name)
# print(os.environ)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
# os.path.join('E:/Python/Python3.6/IO_test','testdir')
# os.mkdir('E:/Python/Python3.6/IO_test/testdir')
s=os.path.split('E:/Python/Python3.6/IO_test/test.txt')
print(s)
g=os.path.splitext('E:/Python/Python3.6/IO_test/test.txt')
print(g)

# os.rename('test01.txt','test03.py')
# os.remove('test03.py')