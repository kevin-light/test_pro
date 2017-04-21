import threading,time
#创建一个子任务
def show(arg):
    time.sleep(1)
    print('thread'+str(arg))
#循环创建10个线程并发执行任务
for i in range(10):
    #创建线程，target=函数，去执行这个函数 args=参数，个这个函数传的参数
    t = threading.Thread(target=show,args=(i,))
    #运行线程：
    t.start()
print('main thread stop')

#z自己创建一个线程类，继承threading.Thread类，重写run方法，start()方法调用内部run()方法
class MyThread(threading.Thread):
    #chushi初始化接受两个参数：
#     def __init__(self,func,args):
#         self.func = func
#         self.args = args
#         #super主动调用父类__init__方法
#         super(MyThread,self).__init__()
#     #执行start()方法，我继承Thread类，他会调用自己run方法，
#     #重写run方法，根据类的继承关系，执行方法找自己然后运行run（）
#     def run(self):
#         self.func(self.args)
# def f2(arg):
#     print(arg)
# for i in range(20):
#     obj = MyThread(f2,i)
#     obj.start()

