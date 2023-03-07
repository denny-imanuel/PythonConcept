from enum import Enum


class Logic:

    def for_loop(self):
        for i in range(0,10,1):
            print(i)

    def nested_loop(self):
        for x in range(0,3,1):
            for y in range(0,5,1):
                print(x,y)

    def and_loop(self):
        xrng = range(0,3,1)
        yrng = range(0,5,1)
        for x,y in zip(xrng, yrng):
            print(x,y)

    def or_loop(self):
        return

    def for_each(self):
        arr = [1,2,3,4,5]
        for i in arr:
            print(i)

    def if_then_else(self):
        val = 0
        if val<0:
            print("Negative")
        elif val>0:
            print("Positive")
        if val==0:
            print("Zero")

    def switch_case(self):
        class Size(Enum):
            S=1
            M=2
            L=3
        my_size = Size.M
        # only on python > 3.10
        match my_size:
            case Size.S:
                print("Small")
            case Size.L:
                print("Large")
            case _:
                print("Medium")

    def while_do(self):
        i = 0
        while i<10:
            print(i)
            i=i+1

    def do_while(self):
        i = 0
        while True:
            print(i)
            i = i+1
            if (i==10):
                break


