import time,threading
#新线程执行：
def loop():
    print('thread %s is runing...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(0.1)
    print('thread %s id ended.' % threading.current_thread().name)
print('thread %s is runing..' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()   #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
print('thread %s ended..' % threading.current_thread().name)

balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100000):
        change_it(n)
t1 = threading.Thread(target=run_thread,args=(5,))
# args=(i,)和args=(i) 前一个参数不固定，后一个参数个数固定的

t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)