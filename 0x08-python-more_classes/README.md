# force method types

def meth1(params) ->return_type : //this checks the expected type

# running expressions

eval(expression, globals=None, locals=None) //default expression
it is used to test code snippets most of the time
example : it executes a string as a py expression
a,b = 5,7
c = eval("a == b") // c = True

exec() //for assigning values and creating variables

to make relation between objects u can declare an attribute outside
the **init** then increment it using class name instead of self inside the init

class C_Name : 
    att1 = 0
    def __init__(self,...):
        ...code...
        C_Name.att1 += 1

# static methods
@staticmethod decorator
