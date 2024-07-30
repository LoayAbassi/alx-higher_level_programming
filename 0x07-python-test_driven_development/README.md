# what is TDD

a method of telling the compiler what results we expect for some inputs
you define a file with all possible errors and what they mean 
like: 
the compiler returns error type so ur test file should contain that error
then the compiler won't show the error and instead it will show what ur file contains for that case
(using docstring)

# Library

unittest

# testing method

self.assertEqual(function,expected_return)


# example using unittest
main.py

{
def add(a, b):
    return a + b
}

test_main.py

{
import unittest
from main import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
}

# what unittest prints 
passes and failures
Number of tests run.
Number of tests passed.
Number of tests failed.
Any errors or failure details.
# example using docstring
def add(a, b):
    """
    Add two numbers and return the result.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# example with doctest

test.txt

{
>>> from main import add
>>> add(2, 3)
5
>>> add(-1, 1)
0
>>> my_function('string', 2)
TypeError: argument must be an integer
}

main.py

{
import doctest
if __name__ == "__main__":
    doctest.testfile("tests.txt")
}

