import json
d=dict(name='bob',age=20,score=99)
print(json.dumps(d))
json_str='{"name": "bob", "age": 20, "score": 99}'
print(json.loads(json_str))

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def __str__(self):
        return 'Studetnt object (%s,%s,%s)' % (self.name,self.age,self.score)
s=Student('bob',20,90)
std_data=json.dumps(s,default=lambda obj: obj.__dict__)
print('Dump Student:',std_data)
rebuild=json.loads(std_data,object_hook=lambda d:Student(d['name'],d['age'],d['score']))
print(rebuild)