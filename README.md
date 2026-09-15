# tangentmode

Automatic differentiation in Python using dual numbers. Supports
arithmetic (`+`, `-`, `*`, `/`, `**`) and elementary functions
(`exp`, `log`, `sin`, `cos`) on `Dual` objects, plus `derivative(f, x)` to get the derivative of any function built from these at a point.

## Installation

```bash
pip install tangentmode
```

## Usage

```python
from tangentmode import Dual, derivative, sin

x = Dual(3, 1)
print(x * x)          # Dual(9, 6)
print(derivative(sin, 0))   # 1.0
```

## How it works

This package uses dual numbers of the form a + bε, where ε² = 0
(and ε ≠ 0). Since ε² = 0, the Taylor expansion of a function f
at a point x + bε collapses to f(x) + f'(x)·b·ε — every higher-order
term vanishes. That means the dual part of the result is exactly
the derivative.

## License

MIT