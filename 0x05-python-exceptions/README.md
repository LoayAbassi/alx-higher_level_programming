#exceptions, using try/except for more secure program running
avoidingsome errors

# appearance

try: # Code that might raise an exception
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("wtvr") // runs if try block completes successfully
finally:
    print("This will always execute.")
    // this block runs whether the exception is raised or not
    // it ensures the code runs no matter what

# multi methods 
it is possible to use multiple except block , but u can simplify it in one block to make code more clear 

{
except TypeError:
    print("wrong type")
    a = 0
except IndexError:
    print("out of range")
    a=0
except ZeroDivisionError:
    print("division by 0")
    a = 0
finally:
    lis.append(a)
 } //this can be simplified to the following

{
except (TypeError, IndexError, ZeroDivisionError) as e:
    if isinstance(e, TypeError): //checking the type of error to print it
        print("wrong type")
    elif isinstance(e, IndexError):
        print("out of range")
    elif isinstance(e, ZeroDivisionError):
        print("division by 0")
    a = 0 // after rinting error changing variable value
}

# raising exceptions 

def raise_exception():
    raise TypeError("This is a type error")

try:
    raise_exception()
except TypeError as te:
    print("Exception raised:", te)


# functions
def f (*args):// this will allow putting any number of args (it's a tuple)