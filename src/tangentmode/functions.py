from .dual import Dual
import math

def derivative(f, x):
    return f(Dual(x, 1)).dual

def exp(x):
    return Dual(math.exp(x.real), math.exp(x.real) * x.dual)

def log(x):
    return Dual(math.log(x.real), x.dual / x.real)

def sin(x):
    return Dual(math.sin(x.real), math.cos(x.real) * x.dual)

def cos(x):
    return Dual(math.cos(x.real), -math.sin(x.real) * x.dual)