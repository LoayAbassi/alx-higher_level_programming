# python like java is OOP language

// it's possible to import a class from another module

# creating a class

class name:
attr1 = None
attr2 = "hi"

    def __init__(self,val1) : //self is the least argument we shoud write
        self.attr1 = val1
    def meth1(self):
        code here

# using it

from fileName import className
obj1 = className(args...) // except self cz it's done automatically
obj1.meth1() ../ caling it


# private / public 
attr declared inside __init__ with self are instances 
attr declared outside __init__ are class attributes
__attr : private
attr : public 
_atr : protected

# to define an empty thing , just write 'pass' in it 
 
# type verification
isinstance(var, type) //returns true if var's type is
                        the same as type in arg

