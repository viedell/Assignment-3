def sheep_profit():
    sheep_count = int(input("Enter number of sheep sold: "))
    base_price = 2500000
    selling_price = 3000000
    total_capital = sheep_count * base_price
    total_revenue = sheep_count * selling_price
    profit = total_revenue - total_capital
    print("Total Capital:", total_capital)
    print("Profit Earned:", profit)

if __name__ == "__main__":
    sheep_profit()