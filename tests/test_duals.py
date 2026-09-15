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
    assert y == Dual(16, 24)

def test_polinomial_function():
    def f(x): return 3*x*x + 2*x + 5
    x = Dual(1, 1)
    y = f(x)
    assert y.dual == 8

def test_commutative_property():
    x = Dual(2, 3)
    assert 2 * x == x * 2

def test_division():
    x = Dual(1, 2)
    y = Dual(2, 3)
    assert x / y == Dual(1 / 2, 1 / 4)

def test_rsub():
    assert 3 - Dual(2, 1) == Dual(1, -1)

def test_rdiv():
    assert 3 / Dual(2, 1) == Dual(3 / 2, -3 / 4)
