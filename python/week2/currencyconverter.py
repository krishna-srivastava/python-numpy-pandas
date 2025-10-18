import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
data = requests.get(url).json()

# response = requests.get(url)
# print(response.status_code)  
# print(response.text)


try:
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., EUR): ").upper()

    rates = data["rates"]
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency code.")

    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]

    print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")

except ValueError:
    print("Invalid input. Please enter a valid number and currency code.")
except Exception as e:
    print("Error:", e)
