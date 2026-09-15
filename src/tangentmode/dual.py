class Dual:
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual
    def __mul__(self, other):
        return Dual(self.real * other.real, self.real * other. dual + self.dual * other.real)
    def __repr__(self):
        return f"Dual({self.real}, {self.dual})"