import tangentmode

def test_cube_of_two():
    def f(x): return x*x*x
    x = Dual(2, 1)
    y = f(x)
    assert y.real == 8
    assert y.dual == 12
