import json
class Student(object):
  def __init__(self,name,age,score):
    self.name=name
    self.age=age
    self.score=score
s=Student('bob',20,89)
print(json.dumps(s))