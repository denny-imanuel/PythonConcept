# generator is a function that yield multiple values (not return a single value)
def simple_generator():
    yield 1
    yield 2
    yield 3

def Main():
    # generator as a function
    for value in simple_generator():
        print(value)
    # generator as an object
    x = simple_generator()
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())

if __name__ == '__main__':
    Main()