from sortedcontainers import SortedList, SortedSet, SortedDict
from collections import deque, Counter, OrderedDict, defaultdict, ChainMap, namedtuple


class Collection:

    def loop_string(self):
        str = "abcde"
        for chr in str:
            print(chr)

    # tuple is immutable data type that can't be changed, both support multiple datatype
    def loop_tuple(self):
        tuple = (1,2,3,'aaa','bbb','ccc')
        for itm in tuple:
            print(itm)

    #list is mutable data type that can be changed, both support multiple datatype
    def loop_list(self):
        list = [1,2,3,'aaa','bbb','ccc']
        for itm in list:
            print(itm)


    def loop_sorted_list(self):
        slist = SortedList([5,4,3,2,1]);
        for itm in slist:
            print(itm)

    def loop_set(self):
        set = {1, 1, 2, 2, 3, 3}
        for itm in set:
            print(itm)

    def loop_sorted_set(self):
        sset = SortedSet({3,3,2,2,1,1})
        for itm in sset:
            print(itm)

    def loop_dict(self):
        dict = {1:'aaa', 2:'bbb', 3:'ccc'}
        dict[4] = 'ddd'
        # loop by items
        for k,v in dict.items():
            print(k,v)
        # loop by keys
        for k in dict.keys():
            print(k,dict[k])
        # loop by values
        for v in dict.values():
            print(v)

    def loop_sorted_dict(self):
        sdict = SortedDict({3:'ccc', 2:'bbb', 1:'aaa'})
        sdict[4] = 'ddd'
        # loop by items
        for k,v in sdict.items():
            print(k,v)
        # loop by keys
        for k in sdict.keys():
            print(k, sdict[k])
        # loop by values
        for v in sdict.values():
            print(v)

    def loop_stack(self):
        stacks = []
        # push operation
        stacks.append('aaa'); print(stacks)
        stacks.append('bbb'); print(stacks)
        stacks.append('ccc'); print(stacks)
        for stack in stacks:
            print(stack)
        # pop operation
        stacks.pop(); print(stacks)
        stacks.pop(); print(stacks)
        stacks.pop(); print(stacks)

    def loop_queue(self):
        queues = []
        # enqueue operation
        queues.append('aaa'); print(queues)
        queues.append('bbb'); print(queues)
        queues.append('ccc'); print(queues)
        for queue in queues:
            print(queue)
        # dequeue operation
        queues.pop(0); print(queues)
        queues.pop(0); print(queues)
        queues.pop(0); print(queues)


        return

    def loop_linked_list(self):
        llist = deque(['bbb']); print(llist)
        llist.appendleft('aaa'); print(llist)
        llist.append('ccc'); print(llist)
        for litm in llist:
            print(litm)
        llist.popleft(); print(llist)
        llist.pop(); print(llist)

    # counter is dictionary data type that contains count of each key
    def loop_counter(self):
        list = ['aaa','aaa','bbb','bbb','ccc','ccc']
        cnt = Counter(list)
        for k,v in cnt.items():
            print(k,v)

    # default dictionary is dictionary data type that can be used to generate the key
    def loop_default_dict(self):
        list = ['aaa','aaa','bbb','bbb','ccc','ccc']
        ddict = defaultdict(int)
        for k,v in enumerate(list):
            ddict[k] = v
        print(ddict)
        for k,v in ddict.items():
            print(k, v)

    # ordered dictionary is not sorted dictionary, it's a dictionary that remember the order of insertion
    def loop_ordered_dict(self):
        dict = {1:'aaa',2:'bbb',3:'ccc'}
        odict = OrderedDict(dict)
        dict.pop(1); dict[1] = 'aaa'
        for k,v in dict.items():
            print(k,v)
        odict.pop(1); odict[1]='aaa'
        for k,v in odict.items():
            print(k,v)

    # chain map is a collection of many dictionaries
    def loop_chain_map(self):
        d1 = {1:'aaa', 2:'bbb', 3:'ccc'}
        d2 = {4:'ddd', 5:'eee', 6:'fff'}
        d3 = {7:'ggg', 8:'hhh', 9:'jjj'}
        cmap = ChainMap(d1,d2,d3)
        for tuple in cmap.items():
            print(tuple)
        for key in cmap.keys():
            print(key)
        for val in cmap.values():
            print(val)

    # named tuple is a tuple datatype that can be created with extra named index
    def loop_named_tuple(self):
        MyTuple = namedtuple('MyTuple', ['key1','key2', 'key3'])
        mytuple = MyTuple('val1','val2','val3')
        print(mytuple[0]); print(mytuple.key1)
        print(mytuple[1]); print(mytuple.key2)
        print(mytuple[2]); print(mytuple.key3)

    # deque is double ended queue datatype or queue datatype that can be enqueue and dequeue from both side
    def loop_deque(self):
        list = ['bbb','ccc','ddd']
        dq = deque(list); print(dq)
        dq.appendleft('aaa'); print(dq)
        dq.popleft(); print(dq)
        dq.append('eee'); print(dq)
        dq.pop(); print(dq)
