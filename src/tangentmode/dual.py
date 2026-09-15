class Dual:
    @staticmethod
    def _to_dual(value: "Dual | float") -> "Dual":
        if isinstance(value, Dual):
            return value
        if isinstance(value, (int, float)):
            return Dual(value, 0)
        raise TypeError(f"Cannot convert {type(value)} to Dual")

    def __init__(self, real: float, dual: float) -> None:
        self.real = real
        self.dual = dual

    def __neg__(self) -> "Dual":
        return Dual(-self.real, -self.dual)

    def __add__(self, other: "Dual | float") -> "Dual":
        other = Dual._to_dual(other)
        return Dual(self.real + other.real, self.dual + other.dual)

    def __radd__(self, other: float) -> "Dual":
        return self + other

    def __sub__(self, other: "Dual | float") -> "Dual":
        other = Dual._to_dual(other)
        return Dual(self.real - other.real, self.dual - other.dual)

    def __rsub__(self, other: float) -> "Dual":
        return -(self - other)

    def __mul__(self, other: "Dual | float") -> "Dual":
        other = Dual._to_dual(other)
        return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)

    def __rmul__(self, other: float) -> "Dual":
        return self * other

    def __truediv__(self, other: "Dual | float") -> "Dual":
        other = Dual._to_dual(other)
        if other.real == 0:
            raise ZeroDivisionError("cannot divide Dual by a value with real part 0")
        return Dual(self.real / other.real, (self.dual * other.real - self.real * other.dual) / (other.real ** 2))

    def __rtruediv__(self, other: float) -> "Dual":
        return Dual(other, 0) / self

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Dual, int, float)):
            return NotImplemented
        other = Dual._to_dual(other)
        return self.real == other.real and self.dual == other.dual

    def __pow__(self, exp: float) -> "Dual":
        if exp == 0:
            return Dual(1, 0)
        return Dual(self.real ** exp, exp * self.real ** (exp - 1) * self.dual)

    def __repr__(self) -> str:
        return f"Dual({self.real}, {self.dual})"