# force method types

def meth1(params) ->return_type : //this checks the expected type

# running expressions
eval(expression, globals=None, locals=None) //default expression
it is used to test code snippets most of the time
example : it executes a string as a py expression 
    a,b = 5,7
    c = eval("a == b") // c = True

exec() //for assigning values and creating variables
