import os,sqlite3
db_file=os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)
conn=sqlite3.connect(db_file)
cursor=conn.cursor()
cursor.execute('create table user(id varchar(20) primary key,name varchar(20),score int)')
cursor.execute(r"insert into user values('A-001','adam',95)")
cursor.execute(r"insert into user values ('A-002','Bart',62)")
cursor.execute(r"insert into user values ('A-003','bjb','78')")
cursor.close()
conn.commit()
conn.close()
def get_score_in(low,hight):
    with sqlite3.connect('test.db') as conn:
        cursor = conn.cursor()
        cursor.execute('select name from user where score between ? and ? order by score', (low,hight))
        result = cursor.fetchall()
        for i in result:
            real_result += i
        return real_result
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('pass')