import numpy as np

class Operation:

    def my_func(self, n):
        return 2 * n

    def builtin_oper(self):
        print(str(123))
        print(int("123"))
        print(bool(1))
        print(bool(0))
        print(list(('aaa', 'bbb', 'ccc')))
        print(dict(one=1, two=2, three=3))
        print(dict(a="aaa", b="bbb", c="ccc"))
        # iteration
        items = iter(["aaa", "bbb", "ccc"])
        for item in items:
            print(item)
        # reversed iteration
        items = reversed(["aaa","bbb","ccc"])
        for item in items:
            print(item)
        # mapping
        inputs = [1,2,3]
        outputs = map(self.my_func, inputs)
        for out in outputs:
            print(out)
        # slicing
        alp = "abcde"
        num = "01234"
        arr = ['aaa','bbb','ccc','ddd','eee']
        print(alp[slice(1,3,1)])
        print(num[slice(1,3,1)])
        print(arr[slice(1,3,1)])
        print(alp[1:3:1])
        print(num[1:3:1])
        print(arr[1:3:1])
        # range/zip/tuple

        return

    def string_oper(self):
        str = " abc 123 !@# "
        alp = "abc"
        num = "123"
        print(str.title())
        print(str.upper())
        print(str.lower())
        print(str.count('c'))
        print(str.find('c'))
        print(str.index('c'))
        print(str.split(' '))
        print(str.partition(' '))
        print(str.strip())
        print(str.replace(' ',''))
        print(str.rjust(25))
        print(str.ljust(25))
        print(str.isalnum())
        print(alp.isalpha())
        print(num.isnumeric())
        print(str[1])

    def list_oper(self):
        pass

    def math_oper(self):
        list = [1,2,3,4,5]
        su = sum(list)
        av = sum(list)/len(list)
        mi = min(list)
        ma = max(list)
        print(su, av, mi, ma)

    def numpy_oper(self):
        list1 = [1,2,3,4,5]
        list2 = [3,3,3,3,3]
        arr1 = np.array(list1)
        arr2 = np.array(list2)
        su = np.sum(arr1)
        av = np.average(arr1)
        me = np.mean(arr1)
        mi = np.min(arr1)
        ma = np.max(arr1)
        print(su, av, me, mi, ma)
        mu = np.multiply(arr1,arr2)
        di = np.divide(arr1,arr2)
        pw = np.power(arr1,arr2)
        sq = np.square(arr1)
        sr = np.sqrt(arr1)
        print(mu,di,pw,sq,sr)

    def my_func(self,a,b):
        return a*b

    def lambda_oper(self):
        x = lambda a : a + 10
        print(x(5))
        x = lambda a,b: a * b
        print(x(3,5))
        x = lambda a,b: self.my_func(a,b)
        print(x(3,5))
        sqr = list(map(lambda x: x**2, range(10)))
        print(sqr)
        sqre = list(filter(lambda y: y!=25, sqr))
        print(sqre)
        tot = list(map(lambda x,y: self.my_func(x,y), range(5), range(5)))
        print(tot)

    def comprehension_oper(self):
        # list comprehension
        sqr = [x**2 for x in range(10)]
        print(sqr)
        # list comprehension with condition filtering
        sqre = [x**2 for x in range(10) if x!=5]
        print(sqre)
        # dictionary comprehension
        sqrd = {x: x**2 for x in range(5)}
        print(sqrd)
        # tuple comprehension
        sqrt = (x**2 for x in range(5))
        print(sqrt)
        # two dim comprehension
        coord = [(x,y) for x in range(5) for y in range(3)]
        print(coord)

    def ternary_oper(self):
        a,b = 10,20
        # use ternary:
        # 'true_val' if 'cond' else 'false_val'
        c = a if a<b else b
        # use tuple:
        # (false_val,true_val)[cond]
        c = (b,a)[a<b]
        # use dictionary:
        # {True:true_val, False:false_val}[cond]
        c = {True:a, False: b}[a<b]
        # use lambda:
        # (lambda:false_val,lambda:true_val)[cond]()
        c = (lambda:b, lambda:a)[a<b]()
        print(c)


if __name__ == '__main__':

    oper = Operation()
    oper.ternary_oper()