# example1: decorator allows you to wrap another function as arguments
import time


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    greeting = func("Hello")   # shout or whisper function is executed here
    print(greeting)


# example2: decorator allow you to wrap another function within decorator function
def execution_time(func):
    def calc(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)  # long_loop function is wrapped and executed here
        end = time.time()
        print("time to execute ", func.__name__, " is ", end - begin)
    return calc


@execution_time  # annotation to call execution_time wrapper function
def long_loop(num):
    for i in range(1, num, 1):
        print(i)
        time.sleep(1)


def Main():
    # greet(shout)
    # greet(whisper)
    long_loop(10)


if __name__ == '__main__':
    Main()
