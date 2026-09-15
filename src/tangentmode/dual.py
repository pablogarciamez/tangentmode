

class Dual:
    @staticmethod
    def _to_dual(value):
        if isinstance(value, Dual):
            return value
        if isinstance(value, (int, float)):
            return Dual(value, 0)
        return NotImplemented

    def __init__(self, real, dual):
        self.real = real
        self.dual = dual

    def __neg__(self):
        return Dual(-self.real, -self.dual)

    def __add__(self, other):
        other = Dual._to_dual(other)
        return Dual(self.real + other.real, self.dual + other.dual)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = Dual._to_dual(other)
        return Dual(self.real - other.real, self.dual - other.dual)

    def __rsub__(self, other):
        return -(self - other)

    def __mul__(self, other):
        other = Dual._to_dual(other)
        return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = Dual._to_dual(other)
        return Dual(self.real / other.real, (self.dual * other.real - self.real * other.dual) / (other.real ** 2))

    def __rtruediv__(self, other):
        return Dual(other, 0) / self

    def __eq__(self, other):
        other = Dual._to_dual(other)
        return self.real == other.real and self.dual == other.dual

    def __repr__(self):
        return f"Dual({self.real}, {self.dual})"