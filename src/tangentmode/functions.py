from .dual import Dual
import math
from typing import Callable

def derivative(f: Callable[[Dual], Dual], x: float) -> float:
    return f(Dual(x, 1)).dual

def exp(x: Dual) -> Dual:
    return Dual(math.exp(x.real), math.exp(x.real) * x.dual)

def log(x: Dual) -> Dual:
    return Dual(math.log(x.real), x.dual / x.real)

def sin(x: Dual) -> Dual:
    return Dual(math.sin(x.real), math.cos(x.real) * x.dual)

def cos(x: Dual) -> Dual:
    return Dual(math.cos(x.real), -math.sin(x.real) * x.dual)