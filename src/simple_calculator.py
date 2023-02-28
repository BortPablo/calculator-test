from dataclasses import dataclass

@dataclass
class SimpleCalculator:
    """A simple calculator class"""
    x: float
    y: float

    def add(self) -> float :
        return self.x + self.y

    def subtract(self) -> float :
        return self.x - self.y

    def multiply(self) -> float:
        return self.x * self.y

    def divide(self) -> float:
        if self.y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.x / self.y
    
    def __repr__(self) -> str:
        return f"SimpleCalculator({self.x}, {self.y})"
    
    def __str__(self) -> str:
        return f"SimpleCalculator({self.x}, {self.y})"

    

if __name__ == "__main__":
    calc = SimpleCalculator(10.2, 7)
    print(calc.add())
    print(calc.subtract())
    print(calc.multiply())
    print(calc.divide())
    print(calc)
    print(str(calc))
    print(calc == SimpleCalculator(10.2, 7))
    