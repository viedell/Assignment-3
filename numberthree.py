def arithmetic_operations():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b if b != 0 else "Undefined (division by zero)")

if __name__ == "__main__":
    arithmetic_operations()