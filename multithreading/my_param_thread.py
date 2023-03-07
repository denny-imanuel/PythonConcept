import threading
from threading import Thread

# run thread as a simple parameterized class
class MyParamThread(Thread):

    def __init__(self, a, b):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b
        self.sum = 0;

    def run(self):
        self.sum = self.a + self.b
        print("Running Param Thread Class " + str(threading.get_native_id()) + " " + str(self.sum))