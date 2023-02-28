from dataclasses import dataclass

@dataclass
class MediumCalculator:
    """A medium calculator class"""
    tot: float

    def add(self, x) -> float:
        if not isinstance(x, (int, float)):
            raise ValueError("Unsupported operand type")
        self.tot += x
        return self.tot

    def subtract(self, x) -> float:
        if not isinstance(x, (int, float)):
            raise ValueError("Unsupported operand type")
        self.tot -= x
        return self.tot
    
    def multiply(self, x) -> float:
        if not isinstance(x, (int, float)):
            raise ValueError("Unsupported operand type")
        self.tot *= x
        return self.tot
    
    def divide(self, x) -> float:
        if not isinstance(x, (int, float)):
            raise ValueError("Unsupported operand type")
        elif x == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.tot /= x
        return self.tot
    
    def power(self, x) -> float:
        if not isinstance(x, (int, float)):
            raise ValueError("Unsupported operand type")
        self.tot **= x
        return self.tot

    def sqrt(self) -> float:
        if self.tot < 0:
            raise ValueError("Cannot take square root of negative number")
        self.tot **= 0.5
        return self.tot
    
    def reset(self) -> float:
        self.tot = 0
        return self.tot
    
    def __repr__(self) -> str:
        return str(self.tot)

    def __str__(self) -> str:
        return str(self.tot)
    
def main () -> None:
    while True:
        try:
            tot = float(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a number")
        
    calc = MediumCalculator(tot)
    while True:
        op = input("Enter an operation (+, -, *, /, **, sqrt, r to reset & q to quit): ")

        if op not in ["+", "-", "*", "/", "**", "sqrt", "r", "q"]:
            print("Invalid operation")
            continue
        if op == "q":
            break
        elif op == "r":
            while True:
                try:
                    tot = float(input("Enter a number: "))
                    break
                except ValueError:
                    print("Please enter a number")
            calc = MediumCalculator(tot)
            continue
        while True:
            if op == "sqrt":
                break
            try:
                x = float(input("Enter a number: "))
                break
            except ValueError:
                print("Please enter a number")

        if op == "+":
            calc.add(x)
        elif op == "-":
            calc.subtract(x)
        elif op == "*":
            calc.multiply(x)
        elif op == "/":
            calc.divide(x)
        elif op == "**":
            calc.power(x)
        elif op == "sqrt":
            calc.sqrt()
    
        print("Result: " + str(calc))
    

if __name__ == "__main__":
    main()