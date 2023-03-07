import threading
from asyncio import sleep
from concurrent.futures import ThreadPoolExecutor


class ThreadPool:

    # run thread as a simple function
    def simple_thread(self):
        print("Running Simple Thread Function " + str(threading.get_native_id()))

    # run thread as a parameterized function
    def param_thread(self, a, b):
        sum = a + b
        print("Running Param Thread Function " + str(threading.get_native_id()) + " " + str(sum))
        return sum

    def exec_simple_function(self):
        executor = ThreadPoolExecutor(5)
        for i in range(1,10,1):
            future = executor.submit(self.simple_thread)
            future.done()
        executor.shutdown()

    def exec_param_function(self):
        executor = ThreadPoolExecutor(5)
        for i in range(1,10,1):
            future = executor.submit(lambda p: self.param_thread(*p), ([10, i]))
            future.done()
            future.result()
        executor.shutdown()
