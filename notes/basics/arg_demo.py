import sys

class FridayError(Exception):
    # this extends standard python exception
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def args_demo(*args):
    print(args)
    print(*args)  # don't use it!
    for arg in args:
        print(arg)

def kwargs_demo(**kwargs):
    print(type(kwargs))
    print(kwargs)
    #print(**kwargs)
    #print(f"Hello {kwargs('Name')}, it is {kwargs('days')}")
    for k in kwargs:
        print(k, kwargs[k])

# this does not work! *(and should not)
def demo(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    if kwargs["day"] == "Friday":
        raise FridayError

def main(argv):
    #print("hello")
    #print(argv)
    #args_demo(1,2,3)
    #kwargs_demo(Name="CS160", days = "Friday")
    demo("CS160", 1, 2, 3, day = "Friday")
    # but not this way!
    demo(1, 2, day ="Friday")

if __name__ == "__main__":
    main(sys.argv)