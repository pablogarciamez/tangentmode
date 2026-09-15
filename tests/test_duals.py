from tangentmode import Dual

def test_cube_of_two():
    def f(x): return x*x*x
    x = Dual(2, 1)
    y = f(x)
    assert y.real == 8
    assert y.dual == 12

def test_dual_squared():
    def f(x): return x*x
    x = Dual(4,3)
    y = f(x)
    assert y != Dual(16, 24)
