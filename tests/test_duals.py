from tangentmode import Dual
from tangentmode import exp, log, sin, cos, derivative
import pytest
import math

def test_cube_of_two():
    def f(x): return x*x*x
    x = Dual(2, 1)
    y = f(x)
    assert y.real == 8
    assert y.dual == 12

def test_pow():
    def f(x): return x ** 3
    x = Dual(2, 1)
    y = f(x)
    assert y == Dual(8, 12)

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

def test_exp():
    assert exp(Dual(0, 1)).real == pytest.approx(1)
    assert exp(Dual(0, 1)).dual == pytest.approx(1)

def test_log():
    assert log(Dual(1, 1)).real == pytest.approx(0)
    assert log(Dual(1, 1)).dual == pytest.approx(1)

def test_sin():
    assert sin(Dual(0, 1)).real == pytest.approx(0)
    assert sin(Dual(0, 1)).dual == pytest.approx(1)

def test_cos():
    assert cos(Dual(0, 1)).real == pytest.approx(1)
    assert cos(Dual(0, 1)).dual == pytest.approx(0)

def test_derivative():
    assert derivative(exp, 0) == pytest.approx(1)

def test_derivative_function_against_aproximation():
    def f(x): return -sin(x) ** 2 - 3 * log(x - 2) + cos(exp(x / log(x)))
    def g(x): return -math.sin(x) ** 2 - 3 * math.log(x - 2) + math.cos(math.exp(x / math.log(x)))
    x = 10
    h = 1e-6
    assert derivative(f, x) == pytest.approx((g(x + h) - g(x - h)) / (2 * h))
