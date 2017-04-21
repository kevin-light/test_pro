import os
def find_file(aStr):
  for dirpath,dirnames,filenames in os.walk('.'):
    for filename in filenames:
      if aStr in filename:
        print('%s/%s' % (dirpath,filename))