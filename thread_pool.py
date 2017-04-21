import queue
import threading
import time
import contextlib

StopEvent = object()
class ThreadPool(object):
    def __init__(self,max_num):
        #创建任务队列:
        self.q = queue.Queue()
        #获取大量数设置
        self.max_num=max_num
        self.treminal = False
        #创建任务线程的list
        self.generate_list=[]
        #创建存放空闲进程的list
        self.free_list=[]
    def run(self,func,args,callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数，回调函数有两个参数1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """
        if len(slef.free_list)==0 and(self.generate_lsit)<self.max_num:
            #创建线程
            self.generate_thread()
        #获取任务
        w = (func,args,callback,)
        #放进队列里面
        self.q.put(w)
    def generate_thread(self):
        #创建一个线程去队列去一个任务执行
        t = threading.Thread(target=self.call)
        t.start()
    def call(self):
        current_thread = threading.currentThread
        self.generate_list.append(current_thread)
        event = self.q.get()
        while event != StopEvent:
            func,arguments,callback = event
            try:
                result = func(*arguments)
                success = True
            except Exception as e:
                success = False
                result = None
            if callback is not None:
                try:
                    callback(success,result)
                except Exception as e:
                    pass
            while self.worker_state(self.free_list,current_thread):
                if self.terminal:
                    event = StopEvent
                else:
                    event = self.q.get()
        else:
            self.generate_lsit.remove(current_thread)
    def close(self):
        full_size = len(self.generate_list)
        while full_size:
            self.q.put(StopEvent)
            full_size -= 1
    def terminate(self):
        self.terminal = True
        while self.generate_list:
            self.q.put(StopEvent)
        self.q.empty()
    @contextlib.contextmanager
    def worker_stant(selfself,state_list,worker_thread):
        state_list.append(worker_thread)
        try:
            yield
        finally:
            state_list.remove(worker_thread)

