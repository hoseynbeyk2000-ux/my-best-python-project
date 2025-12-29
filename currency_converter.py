def convert(amount, from_currency, to_currency):
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "IRR": 42000
    }

    return amount * rates[to_currency] / rates[from_currency]


print("💱 Currency Converter")

amount = float(input("Enter amount: "))
from_currency = input("From (USD / EUR / IRR): ").upper()
to_currency = input("To (USD / EUR / IRR): ").upper()

result = convert(amount, from_currency, to_currency)

print(f"✅ Result: {result:.2f} {to_currency}")
