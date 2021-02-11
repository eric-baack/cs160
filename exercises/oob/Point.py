""" Point.py  """
# Feb 13 2019
import math

class Point:   
    """ Class POint
    x and y must be integers
    """  # this is the doc string, under function
    def __init__(self, _x, _y):    #need to have reference to object itself - self (usually - not keyword) in python; 'this' in other languages
        self._x = _x  # self is never passed as argument - inherent
        self._y = _y   # underscore indicates that these are internal to class point
        if type(self._x) is not int:
            raise TypeError
        if type(self._y) is not int:
            raise TypeError

    def __str__ (self):
        print("bar")
        return f"Point at ({self._x}, {self._y})"  # now controls how object of class is printed

    def __repr__ (self):
        """ called by print"""
        print("foo")
        return f"Point({self._x}, {self._y})"

    #def __lt__ (self, other)
    #    center = Point(0,0)
    #    return (self.distance(center) < other.distance(center)

    def distance (self, other):
        return math.sqrt((self._x - other._x)**2 + (self._y- other._y)**2)

    def get_x (self):
        return self._x

    def set_x (self, new_value):
        set._x = new_value
        return

class Point3D(Point):  # inherits from point
    def __init__ (self, _x_init_value, _y_init_value, _z_init_value):
    # this is a problem - we already know how to set x, y
    # call init function from super class!
        super().__init__(_x_init_value,_y_init_value)
        self._z_coordinate = _z_init_value
    
    def __str__(self):
        return (super().__str__() + print(f"z: {self._z_coordinate}"))


def main():
    print("Point demo")
    p3 = Point3D(1,2, 3)
    print(p3)
    p1 =Point(1,0)
    print(f"((p1.get_x(), p1.y)")
    p2 = Point(2,3)
    try:
        p3 = Point("Hello", [1,2,3])
    except:
        print("ooops")
    print(p2)
    #print(f"Point1 at (p1.x), (p1.y))   # bad!  

if __name__ == "__main__":  # gaurds code against odd behavior when imported
    main()