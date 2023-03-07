import threading
from threading import Thread

from multithreading.my_param_thread import MyParamThread
from multithreading.my_simple_thread import MySimpleThread


class Multithreading:

    # run thread as a simple function
    def simple_thread(self):
        print("Running Simple Thread Function " + str(threading.get_native_id()))

    # run thread as a parameterized function
    def param_thread(self, a, b):
        sum = a + b
        print("Running Param Thread Function " + str(threading.get_native_id()) + " " + str(sum))
        return sum

    def exec_simple_function(self):
        for i in range(1,10,1):
            thread = Thread(target=self.simple_thread)
            thread.start()
            thread.join()

    def exec_param_function(self):
        for i in range(1,10,1):
            thread = Thread(target=self.param_thread, args=(10, i))
            thread.start()
            sum = thread.join()
            print(str(sum))

    def exec_simple_class(self):
        for i in range(1,10,1):
            thread = MySimpleThread()
            thread.start()
            thread.join()

    def exec_param_class(self):
        for i in range(1,10,1):
            thread = MyParamThread(10, i)
            thread.start()
            thread.join()
            print(str(thread.sum))