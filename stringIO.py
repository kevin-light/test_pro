from io import StringIO
# f=StringIO()
# f.write("hello")
# print(f.getvalue())
from io import StringIO
f=StringIO('Hello你好\nhi\ngoodbye!')
while True:
  s=f.readline()
  if s == '':
    break
  print(s.strip())

from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
g=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
f.close