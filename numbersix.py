def swap_variables():
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    x, y = y, x
    print("Swapped Values: x =", x, ", y =", y)

if __name__ == "__main__":
    swap_variables()