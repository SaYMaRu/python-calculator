class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        negative = False

        if a < 0 and b < 0:
            a, b = -a, -b
        elif a < 0 or b < 0:
            negative = True
            a, b = abs(a), abs(b)

        for _ in range(b):
            result += a

        return -result if negative else result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        
        result = 0
        negative = (a < 0) ^ (b < 0) 
        a, b = abs(a), abs(b)

        while a >= b:
            a -= b
            result += 1

        return -result if negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero")

        negative = a < 0
        a = abs(a)

        while a >= b:
            a -= b

        return -a if negative else a
    
# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(5, 2))
    print("Example: multiplication: ", calc.multiply(3, 7))
    print("Example: division: ", calc.divide(5, 2))
    print("Example: modulo: ", calc.modulo(5, 2))