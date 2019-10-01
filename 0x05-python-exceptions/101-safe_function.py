#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        aux = fct(*args)
        return aux
    except Exception as error:
        sys.stderr.write('Exception: {}\n'.format(error))
        return None
