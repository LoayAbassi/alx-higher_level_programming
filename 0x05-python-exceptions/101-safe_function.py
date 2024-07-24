#!/usr/bin/python3
def safe_function(fct, *args):
    """Executes a function safely."""
    try:
        return fct(*args)
    except Exception as e:
        import sys
        sys.stderr.write("Exception: " + str(e) + "\n")
