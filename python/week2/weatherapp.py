import requests

apikey = "your api key"
city = input("Enter your city name: ").lower()
url = f"http://api.weatherapi.com/v1/current.json?key={apikey}&q={city}&aqi=no"

request = requests.get(url)
data = request.json()

# import json
# print(json.dumps(data, indent=4))  # 👈 Pretty print the JSON

if(request.status_code == 200):
    print(f"\nWeather in {city.upper()}")
    print(f"Temperature in celcius: {data["current"]["temp_c"]} °C")
    print(f"Temperature in farenheit: {data["current"]["temp_f"]} °F")
    print(f"Humidity: {data["current"]["humidity"]} %")
    print(f"Wind: {data["current"]["wind_kph"]} Kph")
    print(f"Condition: {data['current']['condition']['text']}")
else:
    print("\nCity not found or API error.")

