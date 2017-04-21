from enum import Enum
Month=Enum('Month',('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'))
for name,member in Month.__members__.items():
  print(name,'=>',member,',',member.value)

from enum import Enum,unique
@unique
class Weekday(Enum):
  Sun=0 #Sun的value被设定为0
  Mon=1
  tue=2
  wed=3
  thu=4
  fri=5
  sat=6
day1=Weekday.Mon
print(day1)
print(Weekday.tue)
print(Weekday['tue'])
print(Weekday.tue.value)
print(day1==Weekday.Mon)
print(Weekday(1))
print(day1==Weekday(1))
for name,member in Weekday.__members__.items():
  print(name,'---',member)