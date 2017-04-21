f=open('E:/Python/Python3.6/IO_test/test.txt','r')
for line in f.readlines():
  print(line.strip())

try:
  f=open('E:/Python/Python3.6/IO_test/test.txt','r')
  print(f.read())
finally:
  if f:
    f.close()

with open('E:/Python/Python3.6/IO_test/test.txt','r') as f:
  print(f.read())

# f=open('E:/Python/Python3.6/IO_test/io_test.png','rb')
# print(f.read())
# f.close()
f=open('E:/Python/Python3.6/IO_test/test.txt','r',encoding='gbk',errors='ignore')
print(f.read())
f.close()

# f=open('E:/Python/Python3.6/IO_test/test.txt','w')
# f.write('hello,world!')
# f.close()
with open('E:/Python/Python3.6/IO_test/test.txt','w') as f:
  f.write('hello,world!')