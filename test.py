import unittest
from src import argtypes

def no_op():
    pass

@argtypes(a=bool, b=callable, c=dict, d=float, e=int, f=list, g=str, h=tuple, i=type(None))
def f1_args(a, b, c, d, e, f, g, h, i):
    pass

@argtypes(a=bool, b=callable, c=dict, d=float, e=int, f=list, g=str, h=tuple, i=type(None))
def f1_kwargs(**kwargs):
    pass

@argtypes(j=(int, list, str))
def f2(j):
    pass

def invalid_argtype(f):
    try:
        f()
        raise Exception('expected TypeError')
    except TypeError:
        pass

def invalid_a():
    f1_kwargs(a=False)

def invalid_b():
    f1_kwargs(b=int())

def invalid_c():
    f1_kwargs(c=list())

def invalid_d():
    f1_kwargs(d=int())

def invalid_e():
    f1_kwargs(e=tuple())

def invalid_f():
    f1_kwargs(f=dict())

def invalid_g():
    f1_kwargs(g=int())

def invalid_h():
    f1_kwargs(h=bool())

def invalid_i():
    f1_kwargs(i=no_op)

def invalid_j():
    f2(j=float())

class TestArgtypes(unittest.TestCase):

    def test_valid_argtypes(self):
        f1_args(False, no_op, {}, 0.0, 0, [], "", (), None)
        f1_kwargs(a=False, b=no_op, c={}, d=0.0, e=0, f=[], g="", h=(), i=None)
        f2(int())
        f2(list())
        f2(str())

    def test_invalid_argtypes(self):
        invalid_argtype(invalid_a)
        invalid_argtype(invalid_b)
        invalid_argtype(invalid_c)
        invalid_argtype(invalid_d)
        invalid_argtype(invalid_e)
        invalid_argtype(invalid_f)
        invalid_argtype(invalid_g)
        invalid_argtype(invalid_h)
        invalid_argtype(invalid_i)
        invalid_argtype(invalid_j)

if __name__ == '__main__':
    unittest.main()