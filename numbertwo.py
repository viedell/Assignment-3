def calculate_change():
    total = int(input("Enter total purchase amount: "))
    paid = int(input("Enter amount paid: "))
    print("Change Returned:", paid - total if paid >= total else "Insufficient payment")

if __name__ == "__main__":
    calculate_change()