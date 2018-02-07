from argtypes import argtypes

def type_error(f, *args):
    try:
        f(*args)
        raise Exception('expected TypeError')
    except TypeError:
        pass

@argtypes(arg=str)
def expects_string(arg):
    pass

@argtypes(arg1=int, arg2=list)
def expects_int_and_list(arg1, arg2):
    pass

@argtypes(arg=(float, tuple))
def expects_float_or_tuple(arg):
    pass

if __name__ == '__main__':

    ## ok
    expects_string('Damn good coffee!')
    expects_int_and_list(8, [1, 2, 3, 4, 5, 6, 7])
    expects_float_or_tuple(0.1)
    expects_float_or_tuple((0, 1))

    ## type errors
    type_error(expects_string, False)
    type_error(expects_int_and_list, 8, ())
    type_error(expects_int_and_list, 'Ducks on a lake!', [1, 2, 3])
    type_error(expects_float_or_tuple, 1)

    print('Done!')