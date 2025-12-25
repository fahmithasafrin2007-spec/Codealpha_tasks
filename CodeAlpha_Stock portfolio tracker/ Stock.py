def show_intro():
    print("=======================================")
    print("         STOCK PORTFOLIO TRACKER       ")
    print("=======================================")
    print("This program calculates your total")
    print("investment based on stock name & quantity.")
    print("=======================================\n")

# Hardcoded dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 150,
    "META": 300
}

def calculate_investment():
    portfolio = {}   # store stock & qty
    total_value = 0

    while True:
        stock = input("Enter stock symbol (AAPL/TSLA/GOOGL/AMZN/META): ").upper()

        if stock not in stock_prices:
            print("❌ Stock not found! Please try again.\n")
            continue

        qty = int(input(f"Enter quantity of {stock}: "))

        cost = qty * stock_prices[stock]
        portfolio[stock] = cost
        total_value += cost

        print(f"Added: {stock} × {qty} = ₹{cost}\n")

        more = input("Add more stocks? (yes/no): ").lower()
        if more == "no":
            break

    return portfolio, total_value


def save_to_file(portfolio, total_value):
    choice = input("Do you want to save the result to a file? (yes/no): ").lower()

    if choice == "yes":
        filename = input("Enter filename (example: result.txt): ")

        with open(filename, "w") as file:
            file.write("----- Stock Portfolio Summary -----\n")
            for stock, value in portfolio.items():
                file.write(f"{stock} : ₹{value}\n")
            file.write(f"\nTOTAL INVESTMENT = ₹{total_value}\n")

        print(f"\n📁 File saved successfully as '{filename}'!")


# MAIN PROGRAM
show_intro()

portfolio, total_value = calculate_investment()

print("=======================================")
print("         PORTFOLIO SUMMARY")
print("=======================================")

for stock, value in portfolio.items():
    print(f"{stock} : ₹{value}")

print("---------------------------------------")
print(f"TOTAL INVESTMENT = ₹{total_value}")
print("=======================================\n")

save_to_file(portfolio, total_value)
