from datetime import datetime,timedelta
now = datetime.now()
print(now)
print(type(now))
dt = datetime(2017,3,10,12,0,0)
print(dt)
print(dt.timestamp())
print(datetime.fromtimestamp(1489118400.0))

print(datetime.utcfromtimestamp(1489118400.0))

cday = datetime.strptime('2017-03-9 11:26:00','%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))

nowa = datetime.now()
print(nowa)
print(nowa+timedelta(hours=10))
print(nowa-timedelta(hours=1))
print(nowa+timedelta(hours=12,days=2))

from datetime import datetime,timedelta,timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

import re
from datetime import datetime,timezone,timedelta
def to_timestamp(dt_str,tz_str):
    print('正则匹配datetime和UTC时区')
    std_ustr = re.match(r'^UTC(\+|\-)0?([0-9]|1[1-2])\:00$',tz_str)
    if std_ustr:
        try:
            time = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
        except BaseException as e:
            print('ValueError:%s is invalid' % e)
    else:
        raise ValueError('Invalid UTC-timezone_string was given.')
    #将时间参数转换为UTC时间
    time = time.replace(tzinfo=timezone.utc)
    #将UTC时区信息转化为int类型参数
    l = list(std_ustr.group(2))
    if l[0] == '0' and l[-1] !='0':
        n = int(l[1])
    else:
        n = int(std_ustr.group(2))
    #根据用户提供的UTC时区信息执行timestamp计算
    if std_ustr.group(1) == '+':
        timestamp = (time - timedelta(hours=n)).timestamp()
    else:
        timestamp = (time + timedelta(hours=n)).timestamp()
    return timestamp
if __name__=='__main__':
    import doctest
    doctest.testmod()