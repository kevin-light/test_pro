# import os
# print('Process (%s) start...' % os.getpid())
# #only works on unix/linux/mac:
# pid = os.fork()
# if pid == 0:
#     print('i am child process (%s) and my parent is %s.' % (os.getpid(),os.getpid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(),pid))

from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))
if __name__=='__main__':
    print('Persent process %s.' % os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child process end.')

from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('task %s runs %0.2f seconds.' % (name,(end - start)))
if __name__=='__main__':
    print('parent process %s.' % os.getpid())
    p=Pool(9)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('earting for all subprocesses done...')
    p.close()
    p.join()
    print('all subprocesses done.')