stocks = {
    "NESTLE": 120,
    "ENGRO": 95,
    "LUCKY": 150,
    "HBL": 180,
    "OGDC": 210
}

print("Available Stocks:", stocks)

stock = input("Enter Stock Name: ").upper()

if stock in stocks:
    quantity = int(input("Enter Quantity: "))

    total = stocks[stock] * quantity

    print("Stock:", stock)
    print("Price:", stocks[stock])
    print("Quantity:", quantity)
    print("Total Investment:", total)

else:
    print("Stock Not Found")