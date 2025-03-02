def right_triangle_metrics():
    base = int(input("Enter base of the triangle: "))
    height = int(input("Enter height of the triangle: "))
    area = 0.5 * base * height
    hypotenuse = (base ** 2 + height ** 2) ** 0.5
    perimeter = base + height + hypotenuse
    print("Area:", area)
    print("Perimeter:", perimeter)

if __name__ == "__main__":
    right_triangle_metrics()
