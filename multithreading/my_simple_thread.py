import threading
from threading import Thread

# run thread as a simple class
class MySimpleThread(Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Running Simple Thread Class " + str(threading.get_native_id()))


