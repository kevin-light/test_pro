#-*- coding:utf-8 -*-
from PIL import Image
im = Image.open('test.png')
print(im.format,im.size,im.mode)